import uuid
from django.db import models
from flights.models import Flights  # adjust import based on actual project structure
from django.contrib.auth.models import User
class Booking(models.Model):
    passenger_name = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField()
    num_seats = models.PositiveIntegerField()
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    flight_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    status = models.CharField(
        max_length=20,
        choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')],
        default='PENDING'
    )
    razorpay_order_id = models.CharField(max_length=255, blank=True, null=True)
    # booking_reference = models.CharField(max_length=20, unique=True, blank=True, editable=False)

    def __str__(self):
        return f"Booking #{self.id} - {self.passenger_name}"

    def save(self, *args, **kwargs):
        if self.flight:
            self.flight_price = self.flight.price
        super().save(*args, **kwargs)
    
    @property
    def total_amount(self):
        return int(self.num_seats * self.flight.price)
