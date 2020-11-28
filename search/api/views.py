from django.shortcuts import render
from rest_framework import  generics
from search.models import *
from .serializer import *
from rest_framework.permissions import AllowAny

# Create your views here.

 
class SearchList(generics.ListCreateAPIView):

    permission_classes = [AllowAny,]
    queryset = Search.objects.all()
    serializer_class = SearchSerializer