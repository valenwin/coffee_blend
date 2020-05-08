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