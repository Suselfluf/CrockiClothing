from turtle import color
from django.db import models

# Create your models here.

class Jacket(models.Model):
    name = models.CharField(max_length=100)
    sizeEu = models.CharField(max_length=10)
    quantity = models.IntegerField()
    color = models.CharField(max_length=20)
    