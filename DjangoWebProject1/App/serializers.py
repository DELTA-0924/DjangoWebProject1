from dataclasses import field
from rest_framework import serializers
from datetime import datetime
from .models import Managers,Apartaments


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Managers;
        fields="__all__"
    def create(self, validated_data):
        validated_data['dataCreated'] = datetime.now()  # ������������� ������� ���� � �����
        return super().create(validated_data)    
        
class ApartamentSerialer(serializers.ModelSerializer):
    class Meta:
        model=Apartaments
        fields="__all__"
    def create(self, validated_data):
        validated_data['date'] = datetime.now()  # ������������� ������� ���� � �����
        return super().create(validated_data)      