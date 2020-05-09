from celery import task
from django.core.mail import EmailMessage
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    email = EmailMessage(subject=subject,
                         body=message,
                         from_email='admin@coffeeblend.com',
                         to=[order.email])
    email.send()
