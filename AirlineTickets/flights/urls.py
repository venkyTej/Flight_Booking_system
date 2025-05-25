from django.urls import path
from . import views

app_name = 'flights'

urlpatterns = [
    path('', views.flight_list, name='list'),
    path('create/', views.flight_create, name='create'),
    path('edit/<int:pk>/', views.flight_edit, name='edit'),
    path('delete/<int:pk>/', views.flight_delete, name='delete'),
    path('view/<int:pk>/', views.flight_detail, name='detail'),

]
