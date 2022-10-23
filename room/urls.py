from django.contrib import admin
from django.urls import path, include
from .views import *
# from rest_framework.authtoken import views
urlpatterns = [
    path('booking_list/',BookingList.as_view(), name='booking-list'),
    path('booking_detail/<int:pk>/',BookingDetails.as_view(), name='booking-detail'),
    path('room_list/',RoomList.as_view(), name='room-list'),
    path('room/<int:pk>/',RoomDetail.as_view(), name='Room-Detail'),
    path('room/<int:pk>/booking/create/', BookingCreate.as_view(), name='booking-create'),

]
