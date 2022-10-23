from urllib import request
from django.shortcuts import get_object_or_404
from .models import*
from room.models import BookingDetail, Room
from .serializers import*
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
import datetime
from rest_framework import status


# mm import request

# from django.utils.dateparse import parse_datetime
# date = parse_datetime(datetime_str)
# Create your views here.


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    response = Response(serializer_class)


class RoomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    response = Response({'message': 'Room not found'})


class BookingList(APIView):
    def get(self, request, format=None):
        bookings = BookingDetail.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)


class BookingCreate(APIView):
    def post(self, request, pk, format=None):
        room = get_object_or_404(Room, pk=pk)
        data = request.data

        check_in = data['check_in']
        check_out = data['check_out']

        check_in = datetime.datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out = datetime.datetime.strptime(check_out, "%Y-%m-%d").date()

        # make sure room is empty between these dates

        # check_in availability
        bookings = BookingDetail.objects.filter(
            room=room, check_in__lte=check_in, check_out__gte=check_in)

        if bookings.exists():
            return Response({"message": "Room is not available during this period"}, status=status.HTTP_409_CONFLICT)

        # check_out availability
        bookings = BookingDetail.objects.filter(
            room=room, check_in__lte=check_out, check_out__gte=check_out)
        if bookings.exists():
            return Response({"message": "Room is not available during this period"}, status=status.HTTP_409_CONFLICT)

        serializer = BookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save(room=room)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookingDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookingDetail.objects.all()
    serializer_class = BookingSerializer
    response = Response({'message': 'Booking not found'})


# class emptyRoom(APIView):
#     def get(self, request, format=None):
#         bookings = BookingDetail.objects.all()
#         serializer = BookingSerializer(bookings, many=True)
#         return Response(serializer.data)

# class emptyRoom(APIView):
#     def get(self, request, format=None):
#         bookings = BookingDetail.objects.all()
#         serializer = BookingSerializer(bookings, many=True)
#         return Response(serializer.data)

