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
    return_flight = models.ForeignKey(
        Flights,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='return_bookings'
    )
    booked_at = models.DateTimeField(auto_now_add=True)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.flight.flight_number} ({self.trip_type})"

    def cancel(self):
        if not self.is_cancelled:
            self.is_cancelled = True

            # Restore seats for main flight
            self.flight.available_seats += self.seats_booked
            self.flight.save()

            # Restore seats for return flight if it's a round trip
            if self.trip_type == 'round' and self.return_flight:
                self.return_flight.available_seats += self.seats_booked
                self.return_flight.save()

            self.save()
