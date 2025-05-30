from django import forms
from .models import Booking
from flights.models import Flights

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'passenger_name', 'aadhar_number', 'email', 
            'flight', 'num_seats'
        ]
        widgets = {
            'passenger_name': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'confirm_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'flight': forms.Select(attrs={'class': 'form-control', 'id': 'flight-select'}),
            'num_seats': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email != confirm_email:
            raise forms.ValidationError("Email and Confirm Email do not match.")

        return cleaned_data

    def save(self, commit=True):
        booking = super().save(commit=False)

        # Auto-fill based on selected flight
        flight = booking.flight
        booking.trip_type = 'round' if flight.is_round_trip else 'single'
