import logging

from django.db import DatabaseError
from django.shortcuts import render
from django.http import HttpResponse

from .models import FoodItem

logger = logging.getLogger(__name__)


def home(request):
    """Display the home page"""
    return render(request, 'home.html')


def orders(request):
    """Display the food menu/orders page with items from database"""
    try:
        italian = FoodItem.objects.filter(category='Italian')
        healthy = FoodItem.objects.filter(category='Healthy')
        desserts = FoodItem.objects.filter(category='Desserts')
        kids = FoodItem.objects.filter(category='Kids')
        spicy = FoodItem.objects.filter(category='Spicy')
    except DatabaseError:
        logger.exception("Failed to fetch food items from the database")
        return render(request, 'orders.html', {
            'italian': [],
            'healthy': [],
            'desserts': [],
            'kids': [],
            'spicy': [],
            'db_error': True,
        }, status=500)

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
    if request.method not in ('GET', 'POST'):
        logger.warning("Unsupported HTTP method %s on payment view", request.method)
        return HttpResponse("Method not allowed", status=405)
    return render(request, 'paymentgateway.html')
