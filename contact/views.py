from django.shortcuts import render
from .forms import ContactUsForm
from .tasks import contact_notification


def contact(request):
    contact_form = ContactUsForm()
    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            cd = contact_form.cleaned_data

            # launch asynchronous task
            contact_notification.delay(cd['name'],
                                       cd['subject'],
                                       cd['email'])
            return render(request, 'contact_success.html')

    return render(request, 'contact.html', {
        'form': contact_form
    })
