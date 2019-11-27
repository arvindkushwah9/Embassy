# Service/serializers.py
from rest_framework import serializers
from . import models
from .models import  Service
from django.utils import timezone

# normal serializer [similar to forms.Form]
class ServiceCreateSerializer(serializers.Serializer):
    title= serializers.CharField(max_length=200)
    description= serializers.CharField()
    image= serializers.ImageField()
    creator_id= serializers.IntegerField(default=1)
    updater_id= serializers.IntegerField(default=1)
    # is called if we save serializer if it do not have an instance
    def create(self, validated_data):
       service = Service.objects.create(**validated_data)     
       return service
    # is called if we save serializer if it have an instance
    def update(self, instance, validated_data):
       instance.__dict__.update(validated_data)       
       instance.save()
       return instance
    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ServiceCreateSerializer, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['title'].required = False
        self.fields['image'].required = False



class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'image','description', 'created_at','creator_id')
        model = models.Service