from django.shortcuts import render
from . models import *
from django.http import JsonResponse
import json

# Create your views here.

def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customers, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        #empty cart for now for non-logges in user    
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping:False'}
        cartItems = Order['get_cart_items']
        
    products = Product.Objects.all()
    context = {'products': products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated.all()
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customers, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        #create empty cart for now for non-logged in user
        items=[]
        order = {'get_cart-total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get-cart_items']


    context = {'items': items, 'order':order, 'cartItems':cartItems }
    return render(request, 'store/cart.html', context)



def checkout(request):
    if request.user.is_authenticated.all()
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customers, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        
    else:
        #create empty cart for now for non-logged in user
        items=[]
        order = {'get_cart-total':0, 'get_cart_items':0, 'shipping': False}
        cartItems = order['get-cart_items']


    context = {'items': items, 'order':order, 'cartItems':cartItems }
    return render(request, 'store/checkout.html', context)



