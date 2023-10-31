from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'avatar', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['email_verified_at']

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
