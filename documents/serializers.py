# Documents/serializers.py
from rest_framework import serializers
from . import models
from .models import  Document
from django.utils import timezone

# normal serializer [similar to forms.Form]
class DocumentCreateSerializer(serializers.Serializer):
    title= serializers.CharField(max_length=200)
    image= serializers.ImageField()
    pub_date= serializers.DateTimeField(default=timezone.now())
    update_date= serializers.DateTimeField(default=timezone.now())
    approved = serializers.BooleanField(default=False)
    creator_id= serializers.IntegerField(default=1)
    updater_id= serializers.IntegerField(default=1)
    # is called if we save serializer if it do not have an instance
    def create(self, validated_data):
       document = Document.objects.create(**validated_data)     
       return document
    # is called if we save serializer if it have an instance
    def update(self, instance, validated_data):
       instance.__dict__.update(validated_data)       
       instance.save()
       return instance

  

# # model serializer [similar to forms.ModelForm]
# class DocumentCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = ('title', 'image')


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id','title', 'approved', 'image', 'created_at')
        model = models.Document