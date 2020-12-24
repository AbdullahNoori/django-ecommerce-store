from django.urls import path 
from . import views

urlspatterns = [
    #Empty string for base url 
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

]