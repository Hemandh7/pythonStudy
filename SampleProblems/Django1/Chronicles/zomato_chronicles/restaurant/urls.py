# restaurant/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/create/', views.dish_create, name='dish_create'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/', views.order_list, name='order_list'),
]
