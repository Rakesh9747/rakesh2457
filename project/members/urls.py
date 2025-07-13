# members/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.testing, name='Member'),
    path('hema/', views.hema, name='Member'),
    path('Descending/', views.Descending, name='Member'),
   
]
