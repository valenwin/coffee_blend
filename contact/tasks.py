from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def contact_notification(name, subject_form, email):
    subject = 'Reservation Coffee Blend'
    body = f"Hi {name},\n"\
           f"Your contact form sent successfully\n"\
           f"Subject: {subject_form}\n"\
           f"Thank you for choosing us."

    email = EmailMessage(subject=subject, body=body,
                         from_email='admin@coffeeblend.com',
                         to=[email])
    email.send()
