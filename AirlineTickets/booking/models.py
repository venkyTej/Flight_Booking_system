from django.db import models
from flights.models import Flights
import uuid 

class Booking(models.Model):
    # CATEGORY_CHOICES = [
    #     ('economy', 'Economy'),
    #     ('business','Business Class')
    # ]
    passenger_name = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()
    num_seats = models.PositiveIntegerField()
    contact_number = models.CharField(max_length=10)
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    # trip_type = models.CharField(max_length=10, choices=TRIP_TYPE_CHOICES)
    # category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    flight_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # booking_reference = models.CharField(max_length=20, unique=True, blank=True, editable=False)

    def __str__(self):
        return f"Booking #{self.id} - {self.passenger_name}"

    def save(self, *args, **kwargs):
        if self.flight:
            self.flight_price = self.flight.price

        # if not self.booking_reference:
        #     self.booking_reference = str(uuid.uuid4()).replace('-', '')[:20].upper()

        super().save(*args, **kwargs)
