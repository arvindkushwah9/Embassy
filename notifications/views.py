from django.shortcuts import render, redirect  

# Create your views here.
from .models import Notification
from django.template import loader
from .forms import NotificationForm
from datetime import datetime
from django.contrib.auth.models import User

from rest_framework import generics

def index(request):
  notifications = Notification.objects.filter(receiver_id=request.user.id)
  context = {'notifications': notifications}
  return render(request, 'notifications/index.html', context)

def new(request):
  print(request.method)
  if request.method == 'GET':
      form = NotificationForm()
  else:
      form = NotificationForm(request.POST)
      user = request.user
      print("Valid form", form.is_valid())

      if form.is_valid():
          print('valid')
          # title = form.cleaned_data['title']
          # image = form.cleaned_data['image']
          instance = form.save(commit=False)
          instance.creator_id = user.id
          instance.updater_id = user.id
          instance.pub_date = datetime.now()
          instance.update_date = datetime.now()
          instance.receiver_id = request.POST['receiver']
          instance.save()
          # form.save()
          return redirect('/notifications')
  users = User.objects.all()
  context = {'users': users}
  return render(request, "notifications/new.html", context)

def show(request):  
    notifications = Notification.objects.all()  
    return render(request,"notifications/show.html",{'notifications':notifications})  

def edit(request, id):  
    notification = Notification.objects.get(id=id)  
    return render(request,'notifications/edit.html', {'notification':notification}) 

def update(request, id):  
    notification = Notification.objects.get(id=id)  
    form = NotificationForm(request.POST, instance = notification)
    if form.is_valid():
        form.save()  
        return redirect("/notifications")  
    return render(request, 'notifications/edit.html', {'notification': notification})  

def destroy(request, id):  
    notification = Notification.objects.get(id=id)  
    notification.delete()  
    return redirect("/notifications")  
