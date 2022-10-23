from django.db import models
import datetime
from .models import*
from django.contrib.auth.models import User
# Create your models here.


class Room(models.Model):

    ROOM_TYPES = (
        ('single-bed', 'single-bed'),
        ('duble-bed', 'duble-bed'),
        ('family-bed', 'family-bed'),
    )
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='room_image',default='room_images/default.jpg')
    room_no = models.CharField(max_length=10)
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    day = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.room_no


class BookingDetail(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room,default=True ,on_delete=models.CASCADE)
    check_in = models.DateField(auto_now=False, auto_now_add=False)
    check_out = models.DateField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User,default=True, on_delete=models.CASCADE)
    no_of_guests = models.IntegerField()
    total_price = models.IntegerField()

    booked_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.room.room_no
