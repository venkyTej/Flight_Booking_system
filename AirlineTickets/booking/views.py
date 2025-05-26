from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Flights, Booking
from .forms import BookingForm

def booking_home(request):
    """
    Display all available flights, with optional search by departure or arrival city.
    """
    query = request.GET.get('q', '')  # Get the search query from the URL
    if query:
        flights = Flights.objects.filter(
            Q(departure_city__icontains=query) |
            Q(arrival_city__icontains=query)
        )
    else:
        flights = Flights.objects.all()

    return render(request, 'booking_home.html', {
        'flights': flights,
        'query': query
    })


def book_flight(request, flight_id):
    """
    Display booking form for a specific flight. Handle booking submission.
    """
    flight = get_object_or_404(Flights, id=flight_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, current_flight=flight)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight
            booking.save()
            return redirect('booking:booking_list')  # Redirect to booking list after booking
    else:
        form = BookingForm(current_flight=flight)

    context = {
        'flight': flight,
        'form': form,
        'base_price': flight.price,
    }

    return render(request, 'book.html', context)


def edit_booking(request, flight_id):
    """
    Edit an existing booking related to a flight.
    """
    booking = get_object_or_404(Booking, flight_id=flight_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking:booking_list')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'edit_booking.html', {'form': form})


def booking_list(request):
    """
    List all bookings.
    """
    bookings = Booking.objects.all().order_by('-booked_at')
    return render(request, 'booking_list.html', {'bookings': bookings})


def cancel_booking(request, booking_id):
    """
    Cancel a booking and restore seat availability.
    """
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == "POST":
        booking.cancel()
        return redirect('booking:booking_list')

    return render(request, 'cancel_confirmation.html', {'booking': booking})
