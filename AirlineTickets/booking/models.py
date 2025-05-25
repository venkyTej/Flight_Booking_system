

from django.db import models
from flights.models import Flights

TRIP_CHOICES = [
    ('single', 'Single Trip'),
    ('round', 'Round Trip'),
]

class Booking(models.Model):
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    seats_booked = models.PositiveIntegerField()
    trip_type = models.CharField(max_length=10, choices=TRIP_CHOICES, default='single')
    return_flight = models.ForeignKey(Flights, on_delete=models.SET_NULL, null=True, blank=True, related_name='return_bookings')
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.flight.flight_number} ({self.trip_type})"
