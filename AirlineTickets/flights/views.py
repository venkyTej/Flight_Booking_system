from django.shortcuts import render, get_object_or_404, redirect
from .models import Flights
from .forms import FlightForm

def flight_list(request):
    flights = Flights.objects.all().order_by('-created_at')
    return render(request, 'flight_list.html', {'flights': flights})

def flight_create(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('flights:list')
    else:
        form = FlightForm()
    return render(request, 'flight_form.html', {'form': form})

def flight_edit(request, pk):
    flight = get_object_or_404(Flights, pk=pk)
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flights:list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flight_form.html', {'form': form})

def flight_delete(request, pk):
    flight = get_object_or_404(Flights, pk=pk)
    flight.delete()
    return redirect('flights:list')

def flight_detail(request, pk):
    flight = get_object_or_404(Flights, pk=pk)
    return render(request, 'views_flight.html', {'flights': flight})

