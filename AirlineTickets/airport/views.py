


from django.shortcuts import render, redirect, get_object_or_404
from .models import Airport
from .forms import AirportForm
# Create your views here.

def airport_list(request):
    airports = Airport.objects.all()
    return render(request, 'view_airport.html', {'airports': airports})

def airport_create(request):
    if request.method == 'POST':
        form = AirportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('airport:airport_list')
    else:
        form = AirportForm()
    return render(request, 'create_airport.html', {'form': form})

def airport_update(request, pk):
    airport = get_object_or_404(Airport, pk=pk)
    if request.method == 'POST':
        form = AirportForm(request.POST, instance=airport)
        if form.is_valid():
            form.save()
            return redirect('airport:airport_list')
    else:
        form = AirportForm(instance=airport)
    return render(request, 'update_airport.html', {'form': form, 'airport': airport})

def airport_delete(request, pk):
    airport = get_object_or_404(Airport, pk=pk)
    if request.method == 'POST':
        airport.delete()
        return redirect('airport:airport_list')
    return render(request, 'delete_airport.html', {'airport': airport})

def airport_list(request):
    airports = Airport.objects.all()
    return render(request, 'airport_list.html', {'airports': airports})






def edit_airport(request, id):
    airport = get_object_or_404(Airport, id=id)
    if request.method == 'POST':
        form = AirportForm(request.POST, request.FILES, instance=airport)
        if form.is_valid():
            form.save()
            return redirect('airport:airport_list')
 
    else:
        form = AirportForm(instance=airport)
    return render(request, 'edit_airport.html', {'form': form})



