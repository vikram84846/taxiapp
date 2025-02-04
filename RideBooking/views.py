from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Ride
from .forms import RideBookingForm
from accounts.models import Profile
# Create your views here.

def book_ride(request):
    if request.method == 'POST':
        form = RideBookingForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.rider = request.user

            # Find an available driver
            available_drivers = Profile.objects.filter(is_driver=True, is_available=True)
            if available_drivers.exists():
                ride.driver = available_drivers.first().user
                ride.status = 'accepted'
                ride.save()

                # Mark the driver as unavailable
                driver_profile = available_drivers.first()
                driver_profile.is_available = False
                driver_profile.save()

                return redirect('ride_status', ride_id=ride.id)
            else:
                # No available drivers
                ride.status = 'requested'
                ride.save()
                return redirect('ride_status', ride_id=ride.id)
    else:
        form = RideBookingForm()
    return render(request, 'book_ride.html', {'form': form})


@login_required
def ride_status(request,ride_id):
    ride = Ride.objects.get(id = ride_id)
    return render(request,"ride_status.html",{"ride":ride})

        