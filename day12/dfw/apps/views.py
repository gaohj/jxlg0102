from django.shortcuts import render

from rest_framework import viewsets
from .models import Book,Game,Movie
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from .serializers import Book3Serializers,GameSerializers,MovieSerializers
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book3Serializers


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializers


# class MovieViewSet(CreateAPIView): #表明这个只允许post 请求
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers

# class MovieViewSet(ListAPIView): #表明这个只允许get 请求
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers


class MovieViewSet(ListCreateAPIView):#表明这个只允许get 和post请求
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers



