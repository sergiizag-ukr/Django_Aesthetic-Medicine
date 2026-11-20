from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action

from .models import (
    Client,
    Service,
    Order,
    Inventory,
    PatientProfile,
)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import (
    ClientSerializer,
    ServiceSerializer,
    OrderSerializer,
)




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
    return render(
        request,
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
    client = get_object_or_404(
        Client,
        id=client_id
    )

    orders = Order.objects.filter(
        client=client
    )

    profile = PatientProfile.objects.filter(
        client=client
    ).first()

    return render(
        request,
        "client_detail.html",
        {
            "client": client,
            "orders": orders,
            "profile": profile,
        }
    )


def order_detail(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id
    )

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

        date_of_birth = request.POST.get(
            "date_of_birth"
        )

        skin_type = request.POST.get(
            "skin_type"
        )

        if Client.objects.filter(
            phone=phone
        ).exists():

            return render(
                request,
                "add_client.html",
                {
                    "error": f"Клієнт з телефоном {phone} вже існує"
                }
            )

        if Client.objects.filter(
            email=email
        ).exists():

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
            date_of_birth=date_of_birth,
            skin_type=skin_type,
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

        client = Client.objects.get(
            id=client_id
        )

        service = Service.objects.get(
            id=service_id
        )

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


def edit_client(request, client_id):

    client = get_object_or_404(
        Client,
        id=client_id
    )

    if request.method == "POST":

        phone = request.POST["phone"]
        email = request.POST["email"]

        if Client.objects.exclude(
            id=client.id
        ).filter(
            phone=phone
        ).exists():

            return render(
                request,
                "edit_client.html",
                {
                    "client": client,
                    "error": f"Клієнт з телефоном {phone} вже існує"
                }
            )

        if Client.objects.exclude(
            id=client.id
        ).filter(
            email=email
        ).exists():

            return render(
                request,
                "edit_client.html",
                {
                    "client": client,
                    "error": f"Клієнт з email {email} вже існує"
                }
            )

        client.first_name = request.POST["first_name"]
        client.last_name = request.POST["last_name"]
        client.phone = phone
        client.email = email
        client.date_of_birth = request.POST.get(
            "date_of_birth"
        )
        client.skin_type = request.POST.get(
            "skin_type"
        )

        client.save()

        return redirect(
            "client_detail",
            client_id=client.id
        )

    return render(
        request,
        "edit_client.html",
        {
            "client": client
        }
    )


def delete_client(request, client_id):

    client = get_object_or_404(
        Client,
        id=client_id
    )

    if request.method == "POST":
        client.delete()
        return redirect("clients")

    return render(
        request,
        "delete_client.html",
        {
            "client": client
        }
    )


def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

        print("=" * 50)
        print(form.errors)
        print("=" * 50)

    else:

        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {
            "form": form
        }
    )


@login_required
def profile(request):

    return render(
        request,
        "profile.html",
        {
            "user": request.user
        }
    )

class OrderAPIView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(
            orders,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class StatisticsAPIView(APIView):

    def get(self, request):
        return Response({
            "clients": Client.objects.count(),
            "services": Service.objects.count(),
            "orders": Order.objects.count(),
        })

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = Order.objects.all()

        status = self.request.query_params.get("status")

        if status:
            queryset = queryset.filter(
                status=status
            )

        return queryset

    @action(detail=True, methods=["post"])
    def complete(self, request, pk=None):
        order = self.get_object()

        order.status = "completed"
        order.save()

        return Response({
            "message": "Order completed"
        })

    def perform_create(self, serializer):
        serializer.save(status="new")