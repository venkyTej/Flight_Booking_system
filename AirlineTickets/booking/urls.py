from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.booking_home, name='booking_home'),
    path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
]


