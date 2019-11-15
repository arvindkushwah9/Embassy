from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    passport_number = forms.CharField(max_length=30, required=False, help_text='Optional.', label="Passport Number")
    phone_number = forms.CharField(max_length=30, required=False, help_text='Optional.', label="Phone Number")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'passport_number', 'phone_number', 'email', 'password1', 'password2', )