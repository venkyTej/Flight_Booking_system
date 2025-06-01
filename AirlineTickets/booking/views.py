from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import BookingForm
from .models import Booking
from flights.models import Flights

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight_price = booking.flight.price
            booking.save()
            return redirect('booking:booking:booking_success', booking.id)  # Using default id
    else:
        form = BookingForm()
    return render(request, 'create_booking.html', {'form': form})

def book_flight(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight_price = booking.flight.price
            booking.total_price = booking.flight.price * booking.num_seats
            booking.save()
            return redirect('booking:booking:booking_success', booking.id)
    else:
        form = BookingForm()
    return render(request, 'booking_form.html', {'form': form})

def booking_success(request, id):  # Changed to id
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'booking_success.html', {'booking': booking})

def get_flight_price(request):
    flight_id = request.GET.get('flight_id')
    if flight_id:
        try:
            flight = Flights.objects.get(id=flight_id)
            return JsonResponse({'price': float(flight.price)})
        except Flights.DoesNotExist:
            return JsonResponse({'error': 'Flight not found'}, status=404)
    return JsonResponse({'error': 'No flight id provided'}, status=400)

def booking_list(request):
    bookings = Booking.objects.all().order_by('-booked_at')
    return render(request, 'booking_list.html', {'bookings': bookings})

def booking_detail(request, id):  # Changed to id
    booking = get_object_or_404(Booking, id=id)
    return render(request, 'booking_detail.html', {'booking': booking})

def cancel_booking(request, id):  # Changed to id
    booking = get_object_or_404(Booking, id=id)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking:booking_list')
    return render(request, 'cancel_booking_confirm.html', {'booking': booking})