from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("clients/", views.clients, name = "clients"),
    path("services/", views.services, name = "services"),
    path("orders/", views.orders, name = "orders"),
    path("clients/<int:client_id>/orders/", views.client_orders, name="client_orders"),
]