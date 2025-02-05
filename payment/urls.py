from django.urls import path
from . import views

urlpatterns = [
    path('payment/<int:ride_id>/', views.payment, name='payment'),
    path('payment/success/', views.payment_success, name='payment_success'),
    path('payment/error/', views.payment_error, name='payment_error'),
]
