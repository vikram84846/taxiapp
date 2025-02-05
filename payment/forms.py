from django import forms

class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, required=True)
    expiry_date = forms.CharField(max_length=5, required=True)
    cvv = forms.CharField(max_length=3, required=True)