from dataclasses import field
from rest_framework import serializers
from .models import *

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'
        
class LoginInfoKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginInfoKey
        fields = '__all__'
        
