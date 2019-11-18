from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title= serializers.CharField(max_length=200)
    description= serializers.CharField()
    content= serializers.CharField()
    image= serializers.ImageField()
    pub_date= serializers.DateTimeField('date published')
    update_date= serializers.DateTimeField('date updated')
