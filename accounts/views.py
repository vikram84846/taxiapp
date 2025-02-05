from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.forms import AuthenticationForm
from RideBooking.models import Ride


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.profile.is_driver = form.cleaned_data.get("is_driver")
            user.profile.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=user,password=password)
            login(request,user)
            return redirect("dashboard")
    else:
        form = UserRegisterForm()
    return render(request,"register.html",{"form":form})


@login_required
def dashboard(request):
    if request.user.profile.is_driver:
        return redirect('driver_pannel')
    else:
        return redirect('rider_pannel')
    

@login_required
def driver_pannel(request):
    if request.user.profile.is_driver:
        active_ride = Ride.objects.filter(driver=request.user, status='accepted').first()
        return render(request, 'driver_pannel.html', {'active_ride': active_ride})
    else:
        return redirect('dashboard')





@login_required
def rider_pannel(request):
    allowed_status = ['requested', 'accepted']
    active_ride = Ride.objects.filter(rider=request.user, status__in=allowed_status).first()
    return render(request, 'rider_pannel.html', {'active_ride': active_ride,"allowed_status":allowed_status})



def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                if user.profile.is_driver:
                    return redirect("driver_pannel")
                else:
                    return redirect("rider_pannel")
    else:
        form = AuthenticationForm()
    return render(request,"login.html",{"form":form})

def user_logout(request):
    logout(request)
    return redirect("login")



def index(request):
    return render(request,"index.html")