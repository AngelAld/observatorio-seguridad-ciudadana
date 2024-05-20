from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EventoListViewSet

router = DefaultRouter()
router.register("eventos", EventoListViewSet, basename="eventos-list")

urlpatterns = [
    path("", include(router.urls)),
]
