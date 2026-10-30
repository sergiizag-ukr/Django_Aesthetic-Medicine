from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("clients/", views.clients, name = "clients"),
    path("services/", views.services, name = "services"),
    path("orders/", views.orders, name = "orders"),
    path("inventory/", views.inventory, name="inventory"),
    path("clients/<int:client_id>/", views.client_detail, name="client_detail"),
    path("orders/<int:order_id>/", views.order_detail, name="order_detail"),
]