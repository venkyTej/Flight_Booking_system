
from django.db import models

class Flights(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Delayed', 'Delayed'),
        ('Cancelled', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20, unique=True)
    airline = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.CharField(max_length=20, blank=True)  # Optional/manual
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seat_capacity = models.PositiveIntegerField(default=180)
    available_seats = models.PositiveIntegerField(default=180)
    is_international = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    image = models.ImageField(upload_to='flight_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.flight_number} - {self.name}"
