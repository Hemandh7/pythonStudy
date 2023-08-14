from django.shortcuts import render, redirect
from .models import Dish, Order


def home(request):
    return render(request, 'home.html')


def menu(request):
    dishes = Dish.objects.all()
    return render(request, 'menu.html', {'dishes': dishes})


def add_dish(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        Dish.objects.create(name=name, price=price)
        return redirect('menu')    


def remove_dish(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    dish.delete()
    return redirect('menu')


def update_dish_availability(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    dish.availability = not dish.availability
    dish.save()
    return redirect('menu')


def take_order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        dish_ids = request.POST.getlist('dish_ids')
        dishes = Dish.objects.filter(pk__in=dish_ids)
        
        total_price = sum(dish.price for dish in dishes)
        
        order = Order.objects.create(customer_name=customer_name)
        order.dishes.set(dishes)
        
        return render(request, 'order_confirmation.html', {'order': order, 'total_price': total_price})
    
    # Handle the case when the request method is not POST
    return redirect('menu')  # Redirect to the menu page if not a POST request

def review_orders(request):
    status_filter = request.GET.get('status_filter', '')
    if status_filter:
        orders = Order.objects.filter(status=status_filter)
    else:
        orders = Order.objects.all()
    
    return render(request, 'review_orders.html', {'orders': orders})


