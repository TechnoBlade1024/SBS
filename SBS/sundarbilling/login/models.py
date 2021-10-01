import datetime

from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    last_login=models.DateTimeField(default=datetime.datetime.now())
class Product(models.Model):
    Quantity=models.IntegerField()

