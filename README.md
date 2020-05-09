# Coffee Blend online shop

## Overview
#### Django3, PostgreSQL

Basic models:<br />
- `Product`
- `Category`
- `Cart`
- `Order`
- `OrderItem`
- `Payment` (using Braintree for order payment)

Other functionality:<br />
- `Celery` launch asynchronous task while order created
- `Export to CSV` for orders (on admin panel)
- `View` link for order details viewing (on admin panel)
    - `admin/order/<int:order_id>/`
- `PDF` link for creation invoice in PDF format (on admin panel)
    - `admin/order/<int:order_id>/pdf/`
- `Sent PDF` to email while order was created