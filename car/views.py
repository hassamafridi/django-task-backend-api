from urllib import request
from django.shortcuts import get_object_or_404
from .models import*
from car.models import  Car
from .serializers import*
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


# mm import request

# from django.utils.dateparse import parse_datetime
# date = parse_datetime(datetime_str)
# Create your views here.

class carpagination(PageNumberPagination):
    page_size =4


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    response = Response(serializer_class)
    pagination_class  = carpagination


class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field='id'
    response = Response({'message': 'Car not found'})