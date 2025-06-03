from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'passenger_name', 'aadhar_number', 'contact_number', 'email',
            'num_seats', 'flight', 'flight_price'
        ]
        widgets = {
            'flight_price': forms.NumberInput(attrs={'readonly': 'readonly'}),
        }
