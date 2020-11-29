from django.shortcuts import render
from rest_framework import  generics,status
from discharge.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny,IsAdminUser,IsAuthenticated,)


class DischargeList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PatientDischargeDetails.objects.all()
    serializer_class = DischargeSerializer


class  DischargeDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset =  PatientDischargeDetails.objects.all()
    serializer_class =  DischargeSerializer
