from rest_framework import viewsets
from .models import CarMake, Car
from .serializers import CarMakeSerializer, CarSerializer

class CarMakeViewSet(viewsets.ModelViewSet):
    queryset = CarMake.objects.all()
    serializer_class = CarMakeSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer