from rest_framework.routers import DefaultRouter

from .views import (
    ClientViewSet,
    ServiceViewSet,
    OrderViewSet,
)

router = DefaultRouter()

router.register(
    r"clients",
    ClientViewSet
)

router.register(
    r"services",
    ServiceViewSet
)

router.register(
    r"orders",
    OrderViewSet,
    basename="orders"
)

urlpatterns = router.urls