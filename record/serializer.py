from rest_framework import serializers
from .models import *


class RecordSerializer(serializers.ModelSerializer):
    # doctorId=serializers.StringRelatedField()

    class Meta:
        model       =       Record
        fields      =       '__all__'
       