from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .forms import BookingForm
from .models import Booking
from flights.models import Flights
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages

@login_required
def bookFlight(request, flight_id):
    '''
    FBV for booking ticket for a flight
    '''
    flight = Flights.objects.get(id=flight_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        print("POST request sent")
        if form.is_valid():
            print("Form valid")
            booking = form.save(commit=False)
            booking.user = request.user
            booking.flight = flight
            booking.save()

            # Construct Razorpay URL with booking ID
            razorpay_url = reverse('payment:create_razorpay_order', args=[booking.id])
            return redirect(razorpay_url)

        else:
            print("Invalid form.")
            print(form.errors)
    else:
        
        form = BookingForm()
    print("Rendering booking form")
    return render(request, 'flight-booking.html', {'form': form, 'flight': flight})


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user = request.user)
    template_name = 'my_bookings.html'
    context = {
        'bookings' : bookings
    }
    return render(request, template_name, context)

def booking_confirm(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_successful') 
    else:
        form = BookingForm()

    flights = Flights.objects.all()
    return render(request, 'booking_form.html', {'form': form, 'flights': flights})



@login_required
def cancel_booking(request, booking_id):
    """
    Cancels a booking if it's still pending and belongs to the logged-in user.
    """
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status == 'COMPLETED':
        messages.error(request, "This booking has already been completed and cannot be cancelled.")
        return redirect('booking:booking_detail', booking_id=booking.id)

    # Optional: if using a 'CANCELLED' status
    booking.status = 'CANCELLED'
    booking.save()

    messages.success(request, "Your booking has been successfully cancelled.")
    return redirect('booking:booking_list')  # Redirect to a booking list or dashboard

def booking_successful(request):
    return render(request, 'booking_successful.html')






def booking_confirmation(request, booking_id):
    booking = Booking.objects.get(booking_reference=booking_id)
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
