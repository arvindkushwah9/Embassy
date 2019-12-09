from django.shortcuts import render, redirect

# Create your views here.
from .models import Service
from django.template import loader
from .forms import ServiceForm
from datetime import datetime
from django.contrib.auth.models import User

from rest_framework import generics
from .serializers import ServiceSerializer, ServiceCreateSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


def index(request):
    services = Service.objects.filter(receiver_id=request.user.id)
    context = {'services': services}
    return render(request, 'services/index.html', context)


def new(request):
    print(request.method)
    if request.method == 'GET':
        form = ServiceForm()
    else:
        form = ServiceForm(request.POST)
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
            return redirect('/services')
    users = User.objects.all()
    context = {'users': users}
    return render(request, "services/new.html", context)


def show(request):
    services = Service.objects.all()
    return render(request, "services/show.html", {'services': services})


def edit(request, id):
    services = Service.objects.get(id=id)
    return render(request, 'services/edit.html', {'services': services})


def update(request, id):
    services = Service.objects.get(id=id)
    form = ServicesForm(request.POST, instance=services)
    if form.is_valid():
        form.save()
        return redirect("/services")
    return render(request, 'services/edit.html', {'services': services})


def destroy(request, id):
    services = Service.objects.get(id=id)
    services.delete()
    return redirect("/services")


@csrf_exempt
@api_view(["GET"])
def services(request):
    services = Service.objects.filter(creator_id=request.user.id)
    # return Response(latest_post_list, status=HTTP_200_OK)
    # the many param informs the serializer that it will be serializing more than a single article.
    serializer = ServiceSerializer(services, many=True)
    return Response({"services": serializer.data})


@api_view(["POST"])
def create_service(request):
    serializer = ServiceCreateSerializer(data=request.data)
    print("Data", request.data)
    print("User", request.user.id)
    if serializer.is_valid():
        # user = Document.objects.create(serializer.validated_data)
        serializer.save(creator=request.user, updater=request.user)
        return Response({"message": "Document created"})
    else:
        data = {
            "error": True,
            "errors": serializer.errors,
        }
        return Response(data)


class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


def socialVisa(request):
    return render(request, 'socialVisa.html')
