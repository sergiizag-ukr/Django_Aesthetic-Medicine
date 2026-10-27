from django.shortcuts import render

ORDERS = [
    {
        "id": 1,
        "client_id": 1,
        "service": "Botox",
        "status": "Completed",
        "price": 5000,
    },
    {
        "id": 2,
        "client_id": 2,
        "service": "Laser Hair Removal",
        "status": "In Progress",
        "price": 3500,
    },
]

# Create your views here.
def home(request):
    return render(
        request,
        "home.html",
        {
            "title": "Beauty Clinic",
            "message": "Вітаємо в системі управління Beauty Clinic",
        }
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
            "clients": [
                {
                    "id": 1,
                    "name": "Anna",
                    "phone": "+380965802384"
                },
                {
                    "id": 2,
                    "name": "Olena",
                    "phone": "+380965912554"
                }
            ]
        }
    )

def services(request):
    return render(
        request,
        "services.html",
        {
            "services": [
                {
                    "id": 1,
                    "name": "Botox",
                    "price": 5000,
                },
                {
                    "id": 2,
                    "name": "Laser Hair Removal",
                    "price": 3500,
                },
                {
                    "id": 3,
                    "name": "Lip Filler",
                    "price": 7000,
                },
                {
                    "id": 4,
                    "name": "Chemical Peel",
                    "price": 2500,
                },
            ]
        }
    )

def orders(request):
    return render(
        request,
        "orders.html",
        {
            "orders": [
                {
                    "id": 1,
                    "client_id": 1,
                    "service": "Botox",
                    "status": "Completed",
                    "price": 5000,
                },
                {
                    "id": 2,
                    "client_id": 2,
                    "service": "Laser Hair Removal",
                    "status": "In Progress",
                    "price": 3500,
                },
            ]
        }
    )


def client_orders(request, client_id):

    filtered_orders = [
        order for order in ORDERS
        if order["client_id"] == client_id
    ]

    return render(
        request,
        "client_orders.html",
        {
            "orders": filtered_orders,
            "client_id": client_id,
        }
    )