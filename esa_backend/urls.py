"""esa_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView # new
from .views import login, sample_api, get_profile, news_api, contact, services, profile, notification, tracking_view, passport_renewal, passport_apply, terms_condition, faq
from documents.views import create_document, tracking
from notifications.views import notifications
from services.views import create_service
api_urlpatterns = [
    path('accounts/', include('rest_registration.api.urls')),
]
urlpatterns = [
    # path('', include('news.urls')),
    path('news/', include('news.urls')),
    path('documents/', include('documents.urls')),
    path('notifications/', include('notifications.urls')),
    path('services/', include('services.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('api/login', login),
    path('', include('sendemail.urls')),

    path('contact', contact),
    path('services', services),
    path('profile', profile),
    path('notification', notification),
    path('tracking', tracking_view),
    path('passport_renewal', passport_renewal),
    path('passport_apply', passport_apply),
    path('terms_condition', terms_condition),
    path('faq', faq),

    # API's path
    path('api/v1/', include(api_urlpatterns)),
    path('api/v1/news', news_api),
    path('api/v1/get_profile', get_profile),
    path('api/v1/', include('documents.urls')),    
    path('api/v1/documents/create_document/', create_document),
    path('api/v1/tracking', tracking),
    path('api/v1/notifications', notifications),
    path('api/v1/', include('services.urls')), 
    path('api/v1/services/create_service/', create_service),


]
