from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json
from django.core import serializers

from django.shortcuts import render
from news.models import Post
from news.serializers import PostSerializer
from accounts.serializers import UserSerializer
from documents.models import Document
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from django.forms.models import model_to_dict


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

@csrf_exempt
@api_view(["GET"])
def news_api(request):
    posts = Post.objects.all()
    # return Response(latest_post_list, status=HTTP_200_OK)
    # the many param informs the serializer that it will be serializing more than a single article.
    serializer = PostSerializer(posts, many=True)
    return Response({"posts": serializer.data})

@api_view(['GET'])
# @authentication_classes([SessionAuthentication, BasicAuthentication])
# @permission_classes([IsAuthenticated])
def get_profile(request, format=None):
    dict_obj = model_to_dict(  request.user )
    return Response({"profile": dict_obj})
    
def contact(request):
  return render(request, 'contact.html')

def services(request):
  return render(request, 'services.html')

def profile(request):
  return render(request, 'profile.html')

def notification(request):
  return render(request, 'notification.html')

def tracking_view(request):
  documents = Document.objects.filter(creator_id=request.user.id)
  context = {'documents': documents}
  return render(request, 'tracking.html', context)

def passport_renewal(request):
  return render(request, 'passport_renewal.html')

def passport_apply(request):
  return render(request, 'passport_apply.html')

def terms_condition(request):
  return render(request, 'terms_condition.html')

def faq(request):
  return render(request, 'faq.html')