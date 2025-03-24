from django.db import models
import datetime

class CarMake(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Car(models.Model):
    class ColorChoices(models.TextChoices):
        RED = "Red"
        BLUE = "Blue"
        BLACK = "Black"
        WHITE = "White"
        GRAY = "Gray"

    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="cars")
    model = models.CharField(max_length=255)
    year = models.IntegerField(default=datetime.datetime.now().year)
    color = models.CharField(max_length=10, choices=ColorChoices.choices)

    def __str__(self):
        return f"{self.year} {self.make.name} {self.model} ({self.color})"