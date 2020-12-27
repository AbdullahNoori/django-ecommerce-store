from django.shortcuts import render
from . models import *

# Create your views here.

def store(request):
    products = Product.Objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated.all()
        customer = request.user.customerorder, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #create empty cart for now for non-logged in user
        items=[]

    context = {}
    return render(request, 'store/cart.html', context)



def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

