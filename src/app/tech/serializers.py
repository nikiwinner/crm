from rest_framework import serializers
from .models import CarMake, Car

class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    make = serializers.PrimaryKeyRelatedField(queryset=CarMake.objects.all())

    class Meta:
        model = Car
        fields = '__all__'