from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import BookingForm
from .models import Booking
from flights.models import Flights


def book_flight(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation') 
    else:
        form = BookingForm()

    flights = Flights.objects.all()
    return render(request, 'booking_form.html', {'form': form, 'flights': flights})



def booking_confirm(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_confirmation') 
    else:
        form = BookingForm()

    flights = Flights.objects.all()
    return render(request, 'booking_form.html', {'form': form, 'flights': flights})



def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            return redirect('booking_confirmation', booking_reference=booking.booking_reference)
    else:
        form = BookingForm()
    return render(request, 'booking_confirmation.html', {'form': form})

def booking_successful(request):
    return render(request, 'booking_successful.html')






def booking_confirmation(request, booking_reference):
    booking = Booking.objects.get(booking_reference=booking_reference)
    return render(request, 'booking_confirmation.html', {'booking': booking})

def cancel_booking(request, booking_reference):
    booking = get_object_or_404(Booking, booking_reference=booking_reference)

    if request.method == 'POST':
        booking.delete()
        return render(request, 'cancel_booking.html', {
            'message': 'Your booking has been cancelled successfully.'
        })

    return render(request, 'cancel_booking.html', {
        'booking': booking,
        'confirm': True
    })
def my_bookings(request):
    bookings = Booking.objects.all().order_by('-booking_date')
    return render(request, 'my_bookings.html', {'bookings': bookings})
