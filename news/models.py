from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from esa_backend.storage_backends import PublicMediaStorage

class Post(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    content= models.TextField()
    image= models.FileField(storage=PublicMediaStorage())
    pub_date= models.DateTimeField('date published')
    update_date= models.DateTimeField('date updated')
    creator= models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)
    updater= models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)