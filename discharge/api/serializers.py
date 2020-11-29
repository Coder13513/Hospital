from rest_framework import serializers
from discharge.models import *


class DischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model       =      PatientDischargeDetails
        fields      =       '__all__'
       