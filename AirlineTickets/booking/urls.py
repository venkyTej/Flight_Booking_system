from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
      # Flight booking form
    path('book/<int:flight_id>', views.bookFlight, name = 'book'),
    path('history/', views.booking_list, name = 'history'),

    
    path('confirmation/<int:booking_id>', views.booking_confirmation, name='booking_confirmation'),
    path('cancel/<str:booking_reference>/', views.cancel_booking, name='cancel_booking'),  # Cancel a booking
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('success/', views.booking_successful, name='booking_successful'),  
  
]


