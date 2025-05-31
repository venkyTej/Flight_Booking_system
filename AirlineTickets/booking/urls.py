from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('new/', views.booking_create, name='booking_create'),
    path('success/<int:booking_id>/', views.booking_success, name='booking_success'),
    path('list/', views.booking_list, name='booking_list'),
    path('detail/<int:booking_id>/', views.booking_detail, name='booking_detail'),  # Fixed duplicate and made singular
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
    path('ajax/get-flight-price/', views.get_flight_price, name='get_flight_price'),
    
    # Optional additions you might want:
    # path('update/<int:booking_id>/', views.booking_update, name='booking_update'),
    # path('print/<int:booking_id>/', views.booking_print, name='booking_print'),
]