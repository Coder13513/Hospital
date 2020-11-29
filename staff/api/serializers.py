from rest_framework import serializers
from staff.models import *


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       Staff
        fields      =       '__all__'
       

