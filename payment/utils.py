from io import BytesIO

import weasyprint
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def payment_pdf_to_email(order):
    subject = 'My Shop - Invoice no. {}'.format(order.id)
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject,
                         message,
                         'admin@coffeeblend.com',
                         [order.email])
    # Create PDF
    html = render_to_string('orders/templates/admin/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach('order_{}.pdf'.format(order.id),
                 out.getvalue(),
                 'application/pdf')
    email.send()
