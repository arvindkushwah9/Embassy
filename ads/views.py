from django.shortcuts import render, redirect  

# Create your views here.
from .models import Ad
from django.template import loader
from .forms import AdForm
from datetime import datetime
from django.contrib.auth.models import User

from rest_framework import generics
from .serializers import AdSerializer, AdCreateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

def index(request):
  # ads = Ad.objects.filter(creator_id=request.user.id)
  ads = Ad.objects.all()
  context = {'ads': ads}
  return render(request, 'ads/index.html', context)

def new(request):
  print(request.method)
  if request.method == 'GET':
      form = AdForm()
  else:
      form = AdForm(request.POST)
      user = request.user
      print("Valid form", form.is_valid())

      if form.is_valid():
          print('valid')
          # title = form.cleaned_data['title']
          # image = form.cleaned_data['image']
          instance = form.save(commit=False)
          instance.creator_id = user.id
          instance.updater_id = user.id
          instance.save()
          # form.save()
          return redirect('/ads')
  users = User.objects.all()
  context = {'users': users}
  return render(request, "ads/new.html", context)

def show(request):  
    ads = Ad.objects.all()  
    return render(request,"ads/show.html",{'ads':ads})  

def edit(request, id):  
    ads = Ad.objects.get(id=id)  
    return render(request,'ads/edit.html', {'ads':ads}) 

def update(request, id):  
    ads = Ad.objects.get(id=id)  
    form = ServicesForm(request.POST, instance = ads)
    if form.is_valid():
        form.save()  
        return redirect("/ads")  
    return render(request, 'ads/edit.html', {'ads': ads})  

def destroy(request, id):  
    ads = Ad.objects.get(id=id)  
    ads.delete()  
    return redirect("/ads")  

@csrf_exempt
@api_view(["GET"])
def ads(request):
    ads = Ad.objects.filter(creator_id=request.user.id)
    # return Response(latest_post_list, status=HTTP_200_OK)
    # the many param informs the serializer that it will be serializing more than a single article.
    serializer = AdSerializer(ads, many=True)
    return Response({"ads": serializer.data})

@api_view(["POST"])
def create_ad(request):
    serializer = AdCreateSerializer(data=request.data)
    print("Data", request.data)
    print("User", request.user.id)
    if serializer.is_valid():
        # user = Ad.objects.create(serializer.validated_data)
        serializer.creater_id = request.user.id 
        serializer.save()
        return Response({"message": "ads created"}) 
    else:
        data = {
          "error": True,
          "errors": serializer.errors,          
        }
        return Response(data) 



class AdList(generics.ListCreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDetail(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    
class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer