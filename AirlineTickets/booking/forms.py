from django import forms
from .models import Booking
from flights.models import Flights

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            
            'passenger_name', 
            'aadhar_number', 
            'contact_number',
            'email', 
            'trip_type', 
            'category',
            'flight', 
            'num_seats'
        ]
        widgets = {
            'booking_id': forms.TextInput(attrs={'class': 'form-control'}),
            'passenger_name': forms.TextInput(attrs={'class': 'form-control'}),
            'aadhar_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'trip_type': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'flight': forms.Select(attrs={
                'class': 'form-control',
                'id': 'flight-select'
            }),
            'num_seats': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

    def save(self, commit=True):
        booking = super().save(commit=False)

        # Auto-fill trip type if based on flight model
        if hasattr(booking.flight, 'is_round_trip') and not booking.trip_type:
            booking.trip_type = 'round' if booking.flight.is_round_trip else 'single'

        if commit:
            booking.save()
        return booking
