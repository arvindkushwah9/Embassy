from rest_framework import serializers
from . import models

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'image', 'pub_date',)
        model = models.Post

class PostSerializer(serializers.Serializer):
    title= serializers.CharField(max_length=200)
    description= serializers.CharField()
    content= serializers.CharField()
    image= serializers.ImageField()
    pub_date= serializers.DateTimeField()
    update_date= serializers.DateTimeField()
