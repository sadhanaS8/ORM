from django.contrib import admin
from .models import Bike_Service,Bike_ServiceAdmin
admin.site.register(Bike_Service, Bike_ServiceAdmin)
