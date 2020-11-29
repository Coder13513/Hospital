from django.shortcuts import render
from rest_framework import  generics
from history.models import *
from .serializers import HistorySerializer
from rest_framework.permissions import (AllowAny,IsAdminUser,IsAuthenticated,)

# Create your views here.

class HistoryList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = History.objects.all()
    serializer_class = HistorySerializer 


class  HistoryDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset =  History.objects.all()
    serializer_class =  HistorySerializer
