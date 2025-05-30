from django.db import models
from django.core.exceptions import ValidationError
from flights.models import Flights


class Booking(models.Model):
    TRIP_CHOICES = [
        ('single', 'Single Trip'),
        ('round', 'Round Trip'),
    ]

    CATEGORY_CHOICES = [
        ('domestic', 'Domestic'),
        ('international', 'International'),
    ]

    passenger_name = models.CharField(max_length=100, null=True)
    aadhar_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True)
    # confirm_email = models.EmailField(null=True)

    trip_type = models.CharField(max_length=10, choices=TRIP_CHOICES)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)

    # This is your foreign key to Flights
    flight = models.ForeignKey(Flights, on_delete=models.SET_NULL, null=True, blank=True)

    num_seats = models.PositiveIntegerField()
    flight_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    

    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    booking_date = models.DateTimeField(auto_now_add=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        if self.email != self.confirm_email:
            raise ValidationError("Email and Confirm Email must match.")

    def save(self, *args, **kwargs):
        if self.flight_price and self.num_seats:
            self.total_price = self.flight_price * self.num_seats
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking #{self.pk} - {self.passenger_name} ({self.flight.flight_number})"
