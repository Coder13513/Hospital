from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import  generics
from record.models import *
from .serializers import RecordSerializer

# Create your views here.

class RecordList(generics.ListCreateAPIView):
    
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
  
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


