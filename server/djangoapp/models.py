# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}: {self.description}'

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('HATCHBACK', 'Hatchback'),
        ('PICKUP', 'Pickup'),
        ('SUV', 'SUV'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    year = models.IntegerField(default=2024,
    validators=[
        MaxValueValidator(2024),
        MinValueValidator(1999)
    ])
    def __str__(self):
        return f'{self.car_make}'