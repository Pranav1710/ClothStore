from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    
    def __str__(self) -> str:
        return f"{self.first_name}"
    