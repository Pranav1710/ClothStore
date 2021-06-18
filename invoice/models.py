from django.db import models
from django.db.models.base import Model, ModelState

# Create your models here.
class Invoice(models.Model):
    customer_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.DecimalFeild(max_digits=7, decimal_places=2)
    
    def __str__(self) -> str:
        return self.name