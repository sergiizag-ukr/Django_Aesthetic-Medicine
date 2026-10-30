from django.contrib import admin
from .models import Client, Service, Order, Inventory


admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Inventory)
