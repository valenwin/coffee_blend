import braintree
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404

from orders.models import Order
from .tasks import payment_completed

gateway = braintree.BraintreeGateway(settings.BRAINTREE_CONF)


def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    total_cost = order.get_total_cost()

    if request.method == 'POST':
        # retrieve nonce
        nonce = request.POST.get('payment_method_nonce', None)
        # create and submit transaction
        result = gateway.transaction.sale({
            'amount': f'{total_cost:.2f}',
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            # mark the order as paid
            order.paid = True
            # store the unique transaction id
            order.braintree_id = result.transaction.id
            order.save()

            # launch asynchronous task
            payment_completed.delay(order.id)
            return redirect('payment:done')
        else:
            # launch asynchronous task
            payment_completed.delay(order.id)
            return redirect('payment:canceled')
    else:
        # generate token
        client_token = gateway.client_token.generate()
        return render(request,
                      'process.html',
                      {'order': order,
                       'total_cost': total_cost,
                       'client_token': client_token})


def payment_done(request):
    return render(request, 'done.html')


def payment_canceled(request):
    return render(request, 'canceled.html')
