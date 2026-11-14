from django.contrib import admin
from .models import Client, Service, Order, Inventory, PatientProfile


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "phone",
        "email",
        "date_of_birth",
        "skin_type",
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "duration_hours",
        "description",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "client",
        "service",
        "status",
        "date",
        "price",
        "completed_at",
    )


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "quantity",
        "min_quantity",
        "category",
        "price",
    )

@admin.register(PatientProfile)
class PatientProfileAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "preferred_procedures",
    )

    search_fields = (
        "client__first_name",
        "client__last_name",
    )