
from django.db import models
from airport.models import Airport

class Flights(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Delayed', 'Delayed'),
        ('Cancelled', 'Cancelled'),
    ]

    CATEGORY = [
        ('economy', 'economy'),
        ('business', 'business')
    ]
    name = models.CharField(max_length=100)
    flight_number = models.CharField(max_length=20)
    airline = models.CharField(max_length=100)
    departure_city = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='flight_dep_airport')
    arrival_city = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='flight_arr_airport')
    departure_time = models.CharField()
    arrival_time = models.CharField()
    duration = models.CharField(max_length=20, blank=True)  # Optional/manual
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seat_capacity = models.PositiveIntegerField(default=180)
    available_seats = models.PositiveIntegerField(default=180)
    is_international = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    image = models.ImageField(upload_to='flight_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, choices=CATEGORY)  # or add choices if needed

    def __str__(self):
        return f"{self.flight_number} - {self.name}"