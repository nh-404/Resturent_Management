# cart/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increment/<int:item_id>/', views.cart_increment, name='cart_increment'),
    path('cart/decrement/<int:item_id>/', views.cart_decrement, name='cart_decrement'),
    path('cart/remove/<int:item_id>/', views.cart_remove, name='cart_remove'),
]
