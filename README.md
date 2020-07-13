# Coffee Blend online shop

## Overview
#### Django3, PostgreSQL, Celery, RabbitMQ

Basic models:<br />
- `Product`
- `Category`
- `Cart`
- `Order`
- `OrderItem`
- `Payment`
- `Coupon` (discount system)
- `Recommender` (recommendation system of products)
- `Reservation`
- `ContactUs`

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
- `Redis` for recommendation system:
    - launch Redis by `redis-server` in terminal
    
## Deploy project on your local machine

1 - To deploy project on your local machine create new virtual environment and execute this command:

`pip install -r requirements.txt`

2 - Insert your own db configuration settings (see example.env):
and change file name to .env:

`SECRET_KEY`,

`DB_PASSWORD`,
`DB_NAME`,
`DB_USER`

`EMAIL_HOST_USER`,
`EMAIL_HOST_PASSWORD`

3 - Migrate db models to PostgreSQL:

`python3 manage.py migrate`

4 - Load data from JSON files:

`python3 manage.py loaddata products.json`
`python3 manage.py loaddata coupons.json`

5 - Run app:

`python3 manage.py runserver`