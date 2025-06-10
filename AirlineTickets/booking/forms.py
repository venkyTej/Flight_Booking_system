from django import forms
from .models import Booking

from django import forms
from django.core.exceptions import ValidationError
from .models import Booking, Flights
import re

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'passenger_name', 'aadhar_number', 'contact_number', 'email',
            'num_seats', 'flight_price'
        ]
        widgets = {
            
            'num_seats': forms.NumberInput(attrs={'id': 'id_num_seats', 'class': 'form-control', 'min': 1}),
            'flight_price': forms.NumberInput(attrs={'readonly': 'readonly', 'class': 'form-control'}),
            'passenger_name': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_passenger_name(self):
        name = self.cleaned_data.get('passenger_name')
        if not re.match(r'^[A-Za-z ]+$', name):
            raise ValidationError("Passenger name should contain only alphabets and spaces.")
        return name

    def clean_aadhar_number(self):
        aadhar = self.cleaned_data.get('aadhar_number')
        if not re.match(r'^\d{12}$', aadhar):
            raise ValidationError("Aadhar number must be exactly 12 digits.")
        return aadhar

    def clean_contact_number(self):
        contact = self.cleaned_data.get('contact_number')
        if not re.match(r'^\d{10}$', contact):
            raise ValidationError("Contact number must be exactly 10 digits.")
        return contact

    def clean_num_seats(self):
        num_seats = self.cleaned_data.get('num_seats')
        if num_seats <= 0:
            raise ValidationError("Number of seats must be greater than 0.")
        return num_seats

    def clean(self):
        cleaned_data = super().clean()
        flight = cleaned_data.get('flight')
        price = cleaned_data.get('flight_price')

        # Ensure flight price matches the selected flight
        if flight and price:
            if price != flight.price:
                raise ValidationError("Flight price mismatch. Please refresh the page or select the correct flight.")
        
        return cleaned_data
