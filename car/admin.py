from django.contrib import admin
from .models import *
# Register your models here.


class CarRoom (admin.ModelAdmin):
    list_display = ['id', 'carname','registrationNo','modalNo', 'image',
                    'category', 'price', 'day']

admin.site.register(Car,CarRoom)