from rest_framework import serializers
from doctor.models import *


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model       =      Doctor
        fields      =       '__all__'
       