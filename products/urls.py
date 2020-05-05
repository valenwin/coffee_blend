from django.urls import path
from .views import MenuListView
from .views import ProductListView, ProductDetailsView


urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('menu/', MenuListView.as_view(), name='product_menu'),
    path('<str:category_slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('product/<str:slug>/', ProductDetailsView.as_view(), name='product_detail'),

]
