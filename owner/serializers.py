from rest_framework import serializers
from .models import *


class ownerSerializer(serializers.ModelSerializer):
    class Meta:
        model = owner
        fields = '__all__'
      


