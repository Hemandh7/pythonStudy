from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('add_dish/', views.add_dish, name='add_dish'),
    path('remove_dish/<int:dish_id>/', views.remove_dish, name='remove_dish'),
    path('update_dish_availability/<int:dish_id>/', views.update_dish_availability, name='update_dish_availability'),
    path('take_order/', views.take_order, name='take_order'),
]
