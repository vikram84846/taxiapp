from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Ride(models.Model):
    STATUS_CHOICES =[
        ("requested","Requested"),
        ("accepted","Accepted"),
        ("completed","Completed"),
        ("cancelled","Cancelled"),
    ]
    LOCATIONS = [
        ("BLOCK-1","B1"),
        ("BLOCK-2","B2"),
        ("BLOCK-3","B3"),
        ("BLOCK-4","B4"),
        ("BLOCK-5","B5"),
        ("BLOCK-6","B6"),
        ("BLOCK-7","B7"),
        ("BLOCK-8","B8"),
        ("BLOCK-9","B9"),
        ("BLOCK-10","B10"),
        ("BLOCK-11","B11"),
        ("BLOCK-12","B12"),
        ("BLOCK-13","B13"),
        ("BLOCK-14","B14"),
        ("BLOCK-15","B15"),


    ]
    rider = models.ForeignKey(User,on_delete=models.CASCADE,related_name="rides_as_rider")
    driver = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="rides_as_driver")
    pickup_location = models.CharField(max_length=20,choices=LOCATIONS)
    destination = models.CharField(max_length=20, choices=LOCATIONS)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES, default="requested")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ride {self.id} - {self.status}"
    
    def calculate_fare(self):
        # Example: Fixed fare of $10
        return 25.00