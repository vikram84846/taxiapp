from django import forms
from .models import Ride

class RideBookingForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ["pickup_location","destination"]
    