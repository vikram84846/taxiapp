from django.urls import path
from . import views
urlpatterns = [
    path('toggle-availability/', views.toggle_availability, name='toggle_availability'),
    path('available-rides/', views.available_rides, name='available_rides'),
    path('accept-ride/<int:ride_id>/', views.accept_ride, name='accept_ride'),
    path('complete-ride/<int:ride_id>/', views.complete_ride, name='complete_ride'),
]
