from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    passport_number = forms.CharField(max_length=30, required=False, help_text='Optional.', label="Passport Number")
    phone_number = forms.IntegerField(required=True, help_text='Optional.', label="Phone Number")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'passport_number', 'phone_number', 'email', 'password1', 'password2', )

class UpdateProfile(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    passport_number = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'passport_number', 'phone_number', 'email',)

    # def clean_email(self):
    #     username = self.cleaned_data.get('username')
    #     email = self.cleaned_data.get('email')

    #     if email and User.objects.filter(email=email).exclude(username=username).count():
    #         raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
    #     return email

    # def save(self, commit=True):
    #     user = super(SignUpForm, self).save(commit=False)
    #     # user.email = self.cleaned_data['email']

    #     if commit:
    #         user.save()

    #     return user