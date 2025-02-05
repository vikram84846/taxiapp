from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from RideBooking.models import Ride
from .models import Payment
from .forms import PaymentForm

@login_required
def payment(request, ride_id):
    ride = Ride.objects.get(id=ride_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            # Simulate payment processing
            card_number = form.cleaned_data['card_number']
            expiry_date = form.cleaned_data['expiry_date']
            cvv = form.cleaned_data['cvv']

            # Create a dummy payment record
            payment = Payment.objects.create(
                ride=ride,
                amount=ride.calculate_fare(),
                is_paid=True,
            )

            # Mark the ride as completed
            ride.status = 'completed'
            ride.save()

            return redirect('payment_success')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {
        'form': form,
        'ride': ride,
    })

@login_required
def payment_success(request):
    return render(request, 'payment_success.html')

@login_required
def payment_error(request):
    return render(request, 'payment_error.html')