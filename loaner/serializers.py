from rest_framework import serializers
from .models import *


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class DhitoDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DhitoDetails
        fields = '__all__'


class PersonContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonContact
        fields = '__all__'
