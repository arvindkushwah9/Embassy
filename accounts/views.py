# accounts/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from  .forms import SignUpForm, UpdateProfile
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .models import UserProfile
from django.contrib.auth.models import User


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'You have signed up successfully')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def profile_update(request):  
    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance = request.user)

        if form.is_valid():
          form.save()

          #Save userinfo record
          # uinfo = form.get_profile()
          # u = User.objects.get(id = request.user.id)
          # uinfo = UserProfile.objects.get_or_create(user=request.user)
          # uinfo =  UserProfile.objects.get(user = u)
          uinfo = request.user.profile
          uinfo.passport_number = request.POST.get('passport_number')
          uinfo.phone_number = request.POST.get('phone_number')
          uinfo.save()

          messages.success(request, 'You have successfully updated')
          return redirect('home')
        else:
          messages.error(request, form.errors)
    else:
        form = SignUpForm()  
    return render(request, 'profile.html', {'form': form}) 