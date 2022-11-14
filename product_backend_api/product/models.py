from django.db import models
from .apps import ProductConfig
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory_quantity = models.IntegerField()
    image = models.CharField(max_length=510, default=ProductConfig.default_image_url)