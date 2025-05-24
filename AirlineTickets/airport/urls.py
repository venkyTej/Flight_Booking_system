from django.urls import path
from . import views

app_name = 'airport'

urlpatterns = [
    path('', views.airport_list, name='airport_list'),  # just '', not 'airport/'
    path('edit/<int:id>/', views.edit_airport, name='edit_airport'),
    path('delete/<int:pk>/', views.airport_delete, name='delete'),
    path('create/', views.airport_create, name='create'),
    path('update/<int:pk>/', views.airport_update, name='update'),
]
