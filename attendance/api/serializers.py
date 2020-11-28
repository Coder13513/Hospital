from rest_framework import serializers
from attendance.models import *


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model       =     Attendance
        fields      =       '__all__'
       