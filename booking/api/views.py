from django.shortcuts import render

# Create your views here.
from booking.models import *
from .serializer import *
from rest_framework import generics
from datetime import datetime


class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class  AppointmentDetail(generics.RetrieveUpdateAPIView):
    queryset =  Appointment.objects.all()
    serializer_class =  AdminAppointmentSerializer

# class  AppointmentDelete(generics.RetrieveUpdateDestroyAPIView):
   
#     serializer_class =  AdminAppointmentSerializer

#     def delete(self, request, *args, **kwargs):
#         queryset =  Appointment.objects.filter(status="Visited")
#         # print Appointment.objects.filter(appointmentDate__lt=datetime.now()).delete()    

#         return self.destroy(request, *args, **kwargs)