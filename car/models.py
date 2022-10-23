from django.db import models
import datetime
from .models import*
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):

    CAR_TYPES = (
        ('car', 'car'),
        ('bus', 'bus'),
        ('Sedan', 'Sedan'),
    )
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='car_image',default='room_images/default.jpg')
    modalNo = models.IntegerField()
    carname= models.CharField(max_length=50)
    registrationNo = models.IntegerField()
    category = models.CharField(max_length=10, choices=CAR_TYPES)
    price = models.IntegerField()
    day = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.carname