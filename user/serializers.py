from rest_framework import serializers
from .models import*
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
# class serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Register
#         fields = '__all__'
#         # fields=('id','name','email','password')
#         # exclude=('password',)
#     # def validate(self, data):
#     #     if data['name']:
#     #         for n in data['name']:
#     #             if n.isdigit():
#     #                 raise serializers.ValidationError(
#     #                     "Name should be numeric not")
#     #     return data


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    ),
    
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # username=serializers.CharField(
    #     required=True,
    #     validators=[UniqueValidator(queryset=User.objects.all())]
    # )
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
 
        # Add custom claims
        token['email'] = user.email
        return token
