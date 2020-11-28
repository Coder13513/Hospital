
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import  generics
from .models import *
from .serializer import HistorySerializer

# Create your views here.

class List(generics.ListCreateAPIView):
    # permission_classes = [IsAdmin|IsSuper]
    queryset = History.objects.all()
    serializer_class = HistorySerializer