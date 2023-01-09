from django.shortcuts import render
from api.models import Article
from api.serializers import Article_serializer, User_serilaizer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
# Create your views here.



class Article_View_Set(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = Article_serializer
    # authentication_classes = (TokenAuthentication) # Closes the whole article page as a form of authentication

class User_View_Set(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = User_serilaizer()
