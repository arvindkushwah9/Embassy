# accounts/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp, name='signup'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    path('profile_update/', views.profile_update),


]