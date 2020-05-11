from django.shortcuts import render, redirect
from .forms import ReserveTableForm
from .tasks import reservation_notification


def reserve_table(request):
    reserve_form = ReserveTableForm()
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        if reserve_form.is_valid():
            cd = reserve_form.cleaned_data
            reserve_form.save()

            # launch asynchronous task
            reservation_notification.delay(cd['first_name'], cd['date'],
                                           cd['time'], cd['email'])
            return render(request, 'reservation_success.html')

    return render(request, 'base.html', {
        'reserve_form': reserve_form
    })
