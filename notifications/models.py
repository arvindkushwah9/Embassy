from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html

# Create your models here.
class Notification(models.Model):
    title= models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')
    update_date= models.DateTimeField('date updated')
    creator= models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)
    updater= models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    receiver = models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)