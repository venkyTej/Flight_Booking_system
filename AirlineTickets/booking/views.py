from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Flights, Booking
from .forms import BookingForm

def booking_home(request):
    query = request.GET.get('q', '')
    
    if query:
        flights = Flights.objects.filter(
            Q(departure_city__icontains=query) |
            Q(arrival_city__icontains=query)
        )
    else:
        flights = Flights.objects.all()

    return render(request, 'home.html', {'flights': flights})

def book_flight(request, flight_id):
    flight = get_object_or_404(Flights, id=flight_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, current_flight=flight)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight
            booking.save()
            return redirect('booking:booking_home')
    else:
        form = BookingForm(current_flight=flight)

    context = {
        'flight': flight,
        'form': form,
        'base_price': flight.price,
    }
    return render(request, 'book.html', context)
