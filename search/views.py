from django.shortcuts import render
from rest_framework import  generics
from .models import *
from .serializer import teacherSerializer

# Create your views here.

class List(generics.ListCreateAPIView):
    # permission_classes = [IsAdmin|IsSuper]
    queryset = Search.objects.all()
    serializer_class = teacherSerializer