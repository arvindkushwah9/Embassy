from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from esa_backend.storage_backends import PublicMediaStorage
# Create your models here.
class Service(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    image= models.FileField(storage=PublicMediaStorage())
    creator= models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)
    updater= models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
