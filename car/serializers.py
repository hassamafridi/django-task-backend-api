from dataclasses import fields
from rest_framework import serializers
from .models import *


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
    # def validate(self, data):
    #     if data['room_no']:
    #         for n in data['room_no']:
    #             if n.isdigit():
    #                 raise serializers.ValidationError(
    #                     "Room number should be numeric not")
    #     return data