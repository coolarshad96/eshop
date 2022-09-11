import email
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(null=True,blank=True)
    phone=models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return str(self.pk)+"-"+self.name
    
    
class Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    address_type=models.CharField(max_length=10,null=True)
    phone=models.CharField(max_length=15,blank=True,null=True)
    address=models.CharField(max_length=100,blank=True,null=True)
    contact_person=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.address
    