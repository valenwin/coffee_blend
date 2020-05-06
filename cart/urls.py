from django.urls import path
from .views import cart_add, cart_details, cart_remove


urlpatterns = [
    path('details/', cart_details, name='cart_detail'),
    path('add/<int:product_id>/', cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),

]
