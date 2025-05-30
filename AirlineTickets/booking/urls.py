from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('new/', views.booking_create, name='booking_create'),
    path('success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('list/', views.booking_list, name='booking_list'),
    path('detail/<int:booking_id>/', views.booking_detail, name='booking_details'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('ajax/get-flight-price/', views.get_flight_price, name='get_flight_price'),
]
