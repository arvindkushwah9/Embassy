from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from rest_framework import generics
from .models import Post
from .serializers import NewsSerializer


def index(request):
  latest_post_list = Post.objects.order_by('-pub_date')[:5]
  context = {'latest_post_list': latest_post_list}
  return render(request, 'news/index.html', context)

def show(request, post_id):
  return HttpResponse("You're looking at post %s." % post_id)

def update(request, post_id):
  response = "You're looking at the results of post %s."
  return HttpResponse(response % post_id)

def edit(request, post_id):
  return HttpResponse("You're voting on post %s." % post_id)

class NewsList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer

class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer