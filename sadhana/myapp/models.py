from django.db import models
from django.contrib import admin

class Bike_Service(models.Model):
    Service_No = models.IntegerField()
    Customer_Name = models.CharField(max_length=20)
    Bike_Model = models.CharField(max_length=20)
    Service_Date = models.DateField()
    Service_Cost = models.FloatField()
    Address = models.TextField()
    Service_Type = models.CharField(max_length=30)

class Bike_ServiceAdmin(admin.ModelAdmin):
    list_display=["Service_No","Customer_Name","Bike_Model","Service_Date","Service_Cost","Address","Service_Type"]






