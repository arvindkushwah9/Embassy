# Documents/serializers.py
from rest_framework import serializers
from . import models


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'image', 'created_at', 'updated_at',)
        model = models.Document