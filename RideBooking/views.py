from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Ride
from .forms import RideBookingForm
from accounts.models import Profile
# Create your views here.

@login_required
def book_ride(request):
    if request.method == 'POST':
        form = RideBookingForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.rider = request.user
            ride.status = 'requested'  # Set status to 'requested' by default
            ride.save()
            return redirect('ride_status', ride_id=ride.id)
    else:
        form = RideBookingForm()
    return render(request, 'book_ride.html', {'form': form})


@login_required
def ride_status(request,ride_id):
    ride = Ride.objects.get(id = ride_id)
    allowed_status = ['requested', 'accepted']
    return render(request,"ride_status.html",{"ride":ride,"allowed_status":allowed_status})

@login_required
def cancel_ride(request, ride_id):
    ride = Ride.objects.get(id=ride_id)

    # Rider can cancel a ride if it's requested or accepted
    if request.user == ride.rider and ride.status in ['requested', 'accepted']:
        ride.status = 'cancelled'
        ride.save()

        # If the ride was accepted, make the driver available again
        if ride.driver:
            driver_profile = ride.driver.profile
            driver_profile.is_available = True
            driver_profile.save()

        return redirect('dashboard')

    # Driver can cancel a ride if it's accepted
    elif request.user.profile.is_driver and ride.status == 'accepted' and ride.driver == request.user:
        ride.status = 'cancelled'
        ride.save()

        # Make the driver available again
        driver_profile = request.user.profile
        driver_profile.is_available = True
        driver_profile.save()

        return redirect('driver_pannel')

    else:
        return redirect('dashboard')

        