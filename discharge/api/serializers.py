from rest_framework import serializers
from discharge.models import *


class DischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model       =      Discharge
        fields      =       '__all__'
       