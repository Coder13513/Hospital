from rest_framework import serializers
from inventory.models import *


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model       =      Inventory
        fields      =       '__all__'
       