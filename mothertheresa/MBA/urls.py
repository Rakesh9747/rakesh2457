# mca/urls.py
from django.urls import path
from . import views

app_name = 'MBA'
urlpatterns = [
    path('', views.home, name='home'),
    # Add other MCA specific URLs
]