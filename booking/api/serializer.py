from rest_framework import serializers
from booking.models import *


class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       Appointment
        fields      =       '__all__'
        read_only_fields        =  ['status']



class AppointmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       Appointment
        fields      =       '__all__'
        