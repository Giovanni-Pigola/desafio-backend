from django.urls import path

from core import views

urlpatterns = [
    path('lastTrips/', views.get_trips, name='lastTrips'),
    path('updateTrips/', views.update_trips, name='lastTrips'),
]
