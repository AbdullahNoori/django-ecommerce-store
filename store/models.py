from django.db import models
from django.contrib.auth.models import User

#CREATE YOUR MODELS HERE

# Create your models here.


class Customer(models.Models):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models. CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    price - models.FlaotField()
    digital - models.BooleanField(default=false, null=true, blank=Ture)
    image = models.ImageField(null-True, blank=True)

class Order(models,Model):
    customer - models.ForeinKey(Customer, on-delete=models.SET_NULL, null-True, blank=True)
    