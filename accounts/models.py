from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	 #required by the auth model
    # user= models.ForeignKey(User, unique=True, related_name="id+", on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, unique=True, related_name='profile', on_delete=models.DO_NOTHING)

    passport_number = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
