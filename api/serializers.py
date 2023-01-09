from rest_framework import serializers
from api.models import Article
from django.contrib.auth.models import User

class Article_serializer(serializers.ModelSerializer): # A CLASS THAT SERIALIZE THE ARTICLE CLASS
    class Meta:
        model = Article
        fields = ["id", "title","description"]

class User_serilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']

        extra_kwargs={'password':{
            'write_only': True,
            'required': True
        }}

    def create(self, Validated_data):
        user = User.objects.create_superuser(**Validated_data)
