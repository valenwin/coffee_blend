# Coffee Blend online shop

## Overview
#### Django3, PostgreSQL

Basic models:<br />
- `Product`
- `Category`
- `Cart`
- `Order`
- `OrderItem`
- `Payment`

Other functionality:<br />
- `Celery` launch asynchronous task while order was created
    - run Celery: `celery -A coffee_blend worker -l info`
- `RabbitMQ` using with Celery for running asynchronous task
    - download RabbitMQ: `www.rabbitmq.com/download.html`
    - run RabbitMQ: `rabbitmq-server` or `brew services run rabbitmq` (MacOS)
- `Braintree` for order payment
    - go to `https://developers.braintreepayments.com/guides/credit-cards/testing-go-live/python` for using test card data
- `Export to CSV` action for orders (on admin panel)
- `View` link for order details viewing (on admin panel)
    - `admin/order/<int:order_id>/`
- `PDF` link for creation invoice in PDF format (on admin panel)
    - `admin/order/<int:order_id>/pdf/`
- `Sent PDF` on email while order was created