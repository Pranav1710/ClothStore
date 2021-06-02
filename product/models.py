from django.db import models
from django.db.models.base import Model, ModelState

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name