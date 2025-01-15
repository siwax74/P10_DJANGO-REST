from rest_framework import serializers
from ..models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'can_be_contacted', 'can_data_be_shared', 'is_active']
        