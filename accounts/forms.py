from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    is_driver = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ["username","email", "password1","password2", "is_driver"]
