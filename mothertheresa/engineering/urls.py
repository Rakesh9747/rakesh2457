# mca/urls.py
from django.urls import path
from . import views

app_name = 'engineering'
urlpatterns = [
    path('', views.home, name='home'),
    # Add other MCA specific URLs
]