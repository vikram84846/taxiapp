from django.shortcuts import render,redirect
from accounts.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from RideBooking.models import Ride
# Create your views here.

@login_required
def toggle_availability(request):
    if request.user.profile.is_driver:
        profile = request.user.profile
        profile.is_available = not profile.is_available
        profile.save()
        return redirect('driver_pannel')
    else:
        return redirect('dashboard')
    
@login_required
def available_rides(request):
    if request.user.profile.is_driver:
        rides = Ride.objects.filter(status='requested')  # Only show requested rides
        return render(request, 'available_rides.html', {'rides': rides})
    else:
        return redirect('dashboard')

@login_required
def accept_ride(request, ride_id):
    if request.user.profile.is_driver:
        ride = Ride.objects.get(id=ride_id)
        if ride.status == 'requested':  # Only accept if the ride is in requested state
            ride.driver = request.user
            ride.status = 'accepted'
            ride.save()

            # Mark the driver as unavailable
            profile = request.user.profile
            profile.is_available = False
            profile.save()

            return redirect('driver_pannel')
        else:
            return redirect('available_rides')
    else:
        return redirect('dashboard')
    

@login_required
def complete_ride(request, ride_id):
    if request.user.profile.is_driver:
        ride = Ride.objects.get(id=ride_id)
        if ride.driver == request.user and ride.status == 'accepted':  # Only complete if the driver is assigned and ride is accepted
            ride.status = 'completed'
            ride.save()

            # Mark the driver as available again
            profile = request.user.profile
            profile.is_available = True
            profile.save()

            return redirect('driver_pannel')
        else:
            return redirect('driver_pannel')
    else:
        return redirect('dashboard')