from django.shortcuts import render
from rest_framework import  generics,status
from doctor.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import (AllowAny,IsAdminUser,IsAuthenticated,)

# Create your views here.

class DoctorList(generics.ListCreateAPIView):

    permission_classes = [IsAdminUser] # (permissions only for if user.is_staff is True)
    queryset = AttendanceDoctors.objects.all()
    serializer_class = AttendanceDoctorsSerializer


class DoctorDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = AttendanceDoctors.objects.all()
    serializer_class = AttendanceDoctorsSerializer  


class StaffList(generics.ListCreateAPIView):

    permission_classes = [IsAdminUser] # (permissions only for if user.is_staff is True)
    queryset = AttendanceStaff.objects.all()
    serializer_class = AttendanceStaffSerializer


class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = AttendanceStaff.objects.all()
    serializer_class = AttendanceStaffSerializer