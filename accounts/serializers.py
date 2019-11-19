from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    username= serializers.CharField(max_length=200)
    email= serializers.CharField()
    pub_date= serializers.DateTimeField()
    update_date= serializers.DateTimeField()