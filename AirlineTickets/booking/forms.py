# booking/forms.py
from django import forms
from .models import Booking, Flights

class BookingForm(forms.ModelForm):
    trip_type = forms.ChoiceField(
        choices=[('single', 'Single Trip'), ('round', 'Round Trip')],
        widget=forms.RadioSelect
    )
    return_flight = forms.ModelChoiceField(
        queryset=Flights.objects.none(),
        required=False
    )

    class Meta:
        model = Booking
        fields = ['name', 'email', 'seats_booked', 'trip_type', 'return_flight']

    def __init__(self, *args, **kwargs):
        current_flight = kwargs.pop('current_flight', None)
        super().__init__(*args, **kwargs)
        if current_flight:
            self.fields['return_flight'].queryset = Flights.objects.filter(
                departure_city=current_flight.arrival_city,
                is_international=current_flight.is_international
            )
        self.fields['seats_booked'].widget.attrs.update({'id': 'id_seats_booked'})
