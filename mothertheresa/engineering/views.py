# mca/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'engineering/home.html', {'title': 'engineering Department'})