from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('book/', views.book_flight, name='booking_create'),  # Flight booking form
    
     path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('cancel/<str:booking_reference>/', views.cancel_booking, name='cancel_booking'),  # Cancel a booking
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('success/', views.booking_successful, name='booking_successful'),  
  
]


