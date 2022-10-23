from django.contrib import admin
from django.urls import path, include
from .views import *
# from rest_framework.authtoken import views
urlpatterns = [
   
    path('car_list/',CarList.as_view(), name='car-list'),
    path('car/<id>',CarDetail.as_view(), name='car-Detail'),

]
