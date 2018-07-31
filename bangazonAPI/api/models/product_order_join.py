from django.db import models
from .product import Product
from .order import Order


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

class Order(models.Model):
# Add in the order fields here
    products = models.ManyToManyField(Product,blank=True)