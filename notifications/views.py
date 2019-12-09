from django.shortcuts import render, redirect  

# Create your views here.
from .models import Notification
from django.template import loader
from .forms import NotificationForm
from datetime import datetime
from django.contrib.auth.models import User

from rest_framework import generics
from .serializers import NotificationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
@api_view(["GET"])
def notifications(request):
    notifications = Notification.objects.filter(receiver_id=request.user.id)
    # return Response(latest_post_list, status=HTTP_200_OK)
    # the many param informs the serializer that it will be serializing more than a single article.
    serializer = NotificationSerializer(notifications, many=True)
    return Response({"notifications": serializer.data})