from celery import shared_task
from django.core.mail import EmailMessage


@shared_task
def reservation_notification(first_name, date, time, email):
    subject = 'Reservation Coffee Blend'
    body = f"Hi {first_name},\n"\
           f"Your reservation confirmed successfully\n"\
           f"Reservation date and time {date} {time}\n"\
           f"Thank you for choosing us."

    email = EmailMessage(subject=subject, body=body,
                         from_email='admin@coffeeblend.com',
                         to=[email])
    email.send()
