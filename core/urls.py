from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("about/", views.about, name = "about"),
    path("clients/", views.clients, name = "clients"),
    path("clients/<int:client_id>/delete/", views.delete_client, name="delete_client"),
    path("clients/<int:client_id>/edit/", views.edit_client, name="edit_client"),
    path("services/", views.services, name = "services"),
    path("orders/", views.orders, name = "orders"),
    path("orders/add/", views.add_order, name="add_order"),
    path("inventory/", views.inventory, name="inventory"),
    path("clients/<int:client_id>/", views.client_detail, name="client_detail"),
    path("orders/<int:order_id>/", views.order_detail, name="order_detail"),
    path("clients/add/", views.add_client, name="add_client"),
]