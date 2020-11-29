from django.shortcuts import render
from rest_framework import  generics
from inventory.models import *
from .serializers import *
from rest_framework.permissions import (AllowAny,IsAdminUser,IsAuthenticated,)

# Create your views here.

class InventoryList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset =stock.objects.all()
    serializer_class = InventorySerializer 


class  InventoryDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset =  stock.objects.all()
    serializer_class = InventorySerializer
