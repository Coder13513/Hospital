from rest_framework import serializers
from .models import *


class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model       =       Search
        fields      =       '__all__'
        read_only_fields        =  ['user']