from rest_framework import serializers
from .models import *


class HistorySerializer(serializers.ModelSerializer):
    # patientId=serializers.StringRelatedField()
    
    class Meta:
        model       =       History
        fields      =       '__all__'
       