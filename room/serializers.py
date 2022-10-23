from dataclasses import fields
from rest_framework import serializers
from .models import *


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
    # def validate(self, data):
    #     if data['room_no']:
    #         for n in data['room_no']:
    #             if n.isdigit():
    #                 raise serializers.ValidationError(
    #                     "Room number should be numeric not")
    #     return data
   


class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer(read_only=True)
    
    class Meta:
        model = BookingDetail
        fields = ( 'id','room', 'check_in','check_out', 'no_of_guests', 'total_price', 'booked_on')


