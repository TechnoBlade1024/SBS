import datetime

from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    last_login=models.DateTimeField(default=datetime.datetime.now())
class Product(models.Model):
    Quantity=models.IntegerField()
    Name=models.CharField(max_length=50)
    Price=models.IntegerField()
    Total_Price=models.IntegerField()
    Billing_Price=models.IntegerField()
    Box_Number=models.IntegerField()
class Bill(models.Model):
    code=models.CharField(max_length=10)
    Customer_id=models.IntegerField()
    Bill_Date=models.DateTimeField()
    Type=models.IntegerField()
class Customer_Details(models.Model):
    Name=models.CharField(max_length=30)
    Shop_name=models.CharField(max_length=30)
    Mobile_Number=models.CharField(max_length=12)
    Alternate_Number=models.CharField(max_length=12)
    Address=models.JSONField()
class Box(models.Model):
    Box_code=models.CharField(max_length=10)



