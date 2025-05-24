from django import forms
from .models import Airport

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = '__all__'
        widgets = {
            'created_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
