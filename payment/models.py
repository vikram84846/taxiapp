from django.db import models
from RideBooking.models import Ride
# Create your models here.

class Payment(models.Model):
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Ride {self.ride.id}"
    
