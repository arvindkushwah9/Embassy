# accounts/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from  .forms import SignUpForm
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm

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