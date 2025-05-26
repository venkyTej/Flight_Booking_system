from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_list, name='booking_list'),  # Main booking list page
    path('home/', views.booking_home, name='booking_home'),  # Optional landing/home page
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),  # Book a specific flight
    path('edit/<int:flight_id>/', views.edit_booking, name='edit_booking'),  # Edit a booking
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),  # Cancel a booking
      # ✅ Added view for all or user-specific bookings
]
