from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodItem

# Create your views here.

def home(request):
    """Display the home page"""
    return render(request, 'home.html')

def orders(request):
    """Display the food menu/orders page with items from database"""
    # Get all food items organized by category
    italian = FoodItem.objects.filter(category='Italian')
    healthy = FoodItem.objects.filter(category='Healthy')
    desserts = FoodItem.objects.filter(category='Desserts')
    kids = FoodItem.objects.filter(category='Kids')
    spicy = FoodItem.objects.filter(category='Spicy')
    
    context = {
        'italian': italian,
        'healthy': healthy,
        'desserts': desserts,
        'kids': kids,
        'spicy': spicy,
    }
    return render(request, 'orders.html', context)

def payment(request):
    """Display the payment gateway"""
    return render(request, 'paymentgateway.html')