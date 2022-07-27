from itertools import product
from pickle import TRUE
from typing_extensions import Self
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True)
    email=models.EmailField(max_length=200,null=True)


def __str__(self):
    return self.name

class Product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(max_length=200,null=True)
    digital=models.BooleanField(default=False,null=True,blank=False)
    
    def __str__(self):
        return self.name
    
    class Order(models.Model):
        customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
        date_ordered=models.DateTimeField(auto_now_add=True)
        complete=models.BooleanField(default=False,null=True,blank=False)
        tramsaction=models.CharField(max_length=200,null=True)
        
        
    def __str__(self):
        return str(self.id)
    
    class OrderItem(models.Model):
        product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
        order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
        quantity=models.IntegerField(default=0,null=True,blank=True)
        
        
        class ShippingAddress(models.Model):
            customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
            order=models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
            address=models.CharField(max_length=200,null=True)
            city=models.CharField(max_length=200,null=True)
            state=models.CharField(max_length=200,null=True)
            zipcode=models.CharField(max_length=200,null=True)
            date_added=models.DateTimeField(auto_now_add=True)
    
    
    
    