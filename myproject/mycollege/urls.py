from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('canteen/', views.canteen_view, name='cateen'),
    path('mess/', views.mess_view, name='mess'),
    path('bakery/', views.bakery_view, name='bekerty'),
    path('cart/', views.cart_view, name='cart'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),


]
