import code
from itertools import product
from multiprocessing.sharedctypes import Value
from operator import mod
from re import U
from statistics import mode
from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,null=True)
    code=models.CharField(max_length=10,null=True,unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    code=models.CharField(max_length=10,null=True, unique=True)

    def __str__(self):
        return self.name

class Seller(models.Model):
    name=models.CharField(max_length=100,null=True)
    code=models.CharField(max_length=100,null=True, unique=True)
    description=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100,null=True)
    sku=models.CharField(max_length=100,null=True, unique=True)
    description=models.CharField(max_length=255,null=True)
    seller=models.ForeignKey(Seller,on_delete=models.SET_NULL,null=True)
    price=models.FloatField()
    old_price=models.FloatField()
    discount=models.FloatField()

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='products')

class Specification(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    rating=models.FloatField()
    review=models.CharField(max_length=255)

    def __str__(self):
        return self.review
    

class ReviewImage(models.Model):
    review=models.ForeignKey(Review, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='reviews')


class Offer(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    subcategory=models.ForeignKey(SubCategory,on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100,null=True)
    code=models.CharField(max_length=100,null=True, unique=True)
    description=models.CharField(max_length=255,null=True)
    offer_type=models.CharField(max_length=100,null=True, unique=True)
    start_at=models.DateTimeField(null=True)
    end_at=models.DateTimeField(null=True)
    offer_value=models.CharField(max_length=100)

    def __str__(self):
        return self.name
