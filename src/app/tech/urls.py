from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarMakeViewSet, CarViewSet

router = DefaultRouter()
router.register(r'carmakes', CarMakeViewSet)
router.register(r'cars', CarViewSet)

urlpatterns = [
    path('', include(router.urls)),
]