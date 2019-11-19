from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Document(models.Model):
    title= models.CharField(max_length=200)
    image= models.ImageField()
    pub_date= models.DateTimeField('date published')
    update_date= models.DateTimeField('date updated')
    creator= models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)
    updater= models.ForeignKey(User, related_name="id+", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('document_edit', kwargs={'pk': self.pk})