from django.shortcuts import render, redirect
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

def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)

    orders = Order.objects.filter(client=client)

    return render(
        request,
        "client_detail.html",
        {
            "client": client,
            "orders": orders,
        }
    )

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)

    return render(
        request,
        "order_detail.html",
        {
            "order": order,
        }
    )

def add_client(request):

    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        phone = request.POST["phone"]
        email = request.POST["email"]

        if Client.objects.filter(phone=phone).exists():

            return render(
                request,
                "add_client.html",
                {
                    "error": f"Клієнт з телефоном {phone} вже існує"
                }
            )

        if Client.objects.filter(email=email).exists():

            return render(
                request,
                "add_client.html",
                {
                    "error": f"Клієнт з email {email} вже існує"
                }
            )

        Client.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            email=email,
        )

        return redirect("clients")

    return render(
        request,
        "add_client.html"
    )

def add_order(request):

    if request.method == "POST":

        client_id = request.POST["client"]
        service_id = request.POST["service"]
        status = request.POST["status"]

        client = Client.objects.get(id=client_id)
        service = Service.objects.get(id=service_id)

        Order.objects.create(
            client=client,
            service=service,
            status=status,
            price=service.price,
        )

        return redirect("orders")

    return render(
        request,
        "add_order.html",
        {
            "clients": Client.objects.all(),
            "services": Service.objects.all(),
        }
    )