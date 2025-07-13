from django.shortcuts import render
from .models import CanteenItem, MessItem, BakeryItem

def home_view(request):
    latest_item = CanteenItem.objects.order_by('-id').first()
    return render(request, 'home.html', {'latest_item': latest_item})

def canteen_view(request):
    items = CanteenItem.objects.all()
    return render(request, 'canteen_list.html', {'items': items})

def mess_view(request):
    items = MessItem.objects.all()
    return render(request, 'mess_list.html', {'items': items})

def bakery_view(request):
    items = BakeryItem.objects.all()
    return render(request, 'bakery_list.html', {'items': items})
