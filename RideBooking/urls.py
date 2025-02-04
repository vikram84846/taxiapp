from django.urls import path
from . import views
urlpatterns = [
    path("book-ride/",views.book_ride,name= "book_ride"),
    path("ride-status/<int:ride_id>",views.ride_status,name="ride_status"),
    path('cancel-ride/<int:ride_id>/', views.cancel_ride, name='cancel_ride'),
]
