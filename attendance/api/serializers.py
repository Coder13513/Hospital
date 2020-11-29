from rest_framework import serializers
from attendance.models import *


class AttendanceDoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     AttendanceDoctors
        fields      =       '__all__'  


class AttendanceStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     AttendanceStaff
        fields      =       '__all__'
       
       