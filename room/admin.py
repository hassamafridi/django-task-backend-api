from django.contrib import admin
from .models import *
# Register your models here.


class adminRoom (admin.ModelAdmin):
    list_display = ['id', 'room_no', 'image',
                    'room_type', 'price', 'is_available', 'day',]


class adminBooking (admin.ModelAdmin):
    list_display = ['id', 'user','room', 'check_in', 'check_out',
                    'no_of_guests', 'total_price', 'booked_on',]


admin.site.register(Room, adminRoom)
admin.site.register(BookingDetail, adminBooking)
