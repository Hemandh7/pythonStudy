# restaurant/views.py

from django.shortcuts import render, redirect
from .models import Dish, Order
from .forms import DishForm

def dish_list(request):
    dishes = Dish.objects.all()
    return render(request, 'restaurant/dish_list.html', {'dishes': dishes})

def dish_create(request):
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dish_list')
    else:
        form = DishForm()
    return render(request, 'restaurant/dish_form.html', {'form': form})

def create_order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        dish_ids = request.POST.getlist('dishes')
        
        order = Order.objects.create(customer_name=customer_name, status='received')
        for dish_id in dish_ids:
            order.dishes.add(dish_id)
        
        return redirect('order_list')

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/order_list.html', {'orders': orders})
