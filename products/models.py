from django.db import models

# Create your models here.
from picklefield import PickledObjectField


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.BigIntegerField()
    properties = PickledObjectField()
