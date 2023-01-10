from api.models import Article
from api.serializers import Article_serializer, User_serilaizer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

# Create your views here.



class Article_View_Set(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    authentication_classes = (TokenAuthentication,)

class User_View_Set(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serilaizer
