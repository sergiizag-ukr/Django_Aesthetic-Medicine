from django.shortcuts import render
from .models import Client, Service, Order, Inventory

# Create your views here.
def home(request):
    context = {
        "title": "Beauty Clinic",
        "message": "Вітаємо в системі управління Beauty Clinic",
        "total_clients": Client.objects.count(),
        "total_orders": Order.objects.count(),
        "total_services": Service.objects.count(),
    }

    return render(
        request,
        "home.html",
        context
    )

def about(request):
    return render(request,
                "about.html",
                {
                    "title": "Aesthetic Medicine",
                    "text": "Beauty Clinic Management System - це навчальний Django-проект для управління клієнтами, косметологічними послугами та замовленнями в клініці естетичної медицини",
                }
            )

def clients(request):
    return render(
        request,
        "clients.html",
        {
            "clients": Client.objects.all(),
        }
    )

def services(request):
    return render(
        request,
        "services.html",
        {
            "services": Service.objects.all(),
        }
    )

def orders(request):
    return render(
        request,
        "orders.html",
        {
            "orders": Order.objects.all(),
        }
    )

def inventory(request):
    return render(
        request,
        "inventory.html",
        {
            "inventory": Inventory.objects.all()
        }
    )