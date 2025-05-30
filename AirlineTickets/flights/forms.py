from django import forms
from .models import Flights

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flights
        fields = '__all__'
        widgets = {
            'departure_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }



