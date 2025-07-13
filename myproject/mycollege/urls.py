from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('canteen/', views.canteen_view, name='canteen'),
    path('mess/', views.mess_view, name='mess'),
    path('bakery/', views.bakery_view, name='bakery'),
]
