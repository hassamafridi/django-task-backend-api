from django.shortcuts import render
from .models import*
from .serializers import*
from rest_framework import generics
# Create your views here.
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
    


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
# class registerapi(generics.ListCreateAPIView):
#     queryset = Register.objects.all()
#     serializer_class = serializer


# class registerapi1(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Register.objects.all()
#     serializer_class = serializer
#     lookup_url_kwarg = 'id'
 # def get(self,request):
 #     register_objs=Register.objects.all()
 #     serializer_objs=serializer(register_objs,many=True)
 #     return Response(serializer_objs.data)

 # def post(self,request):
 #     serializer_objs=serializer(data=request.data)
 #     if serializer_objs.is_valid():
 #         serializer_objs.save()
 #         return Response(serializer_objs.data)
 #     return Response(serializer_objs.errors)
 # def put(self,request):
 #     register_objs=Register.objects.get(id=request.data['id'])
 #     serializer_objs=serializer(register_objs,data=request.data)
 #     if serializer_objs.is_valid():
 #         serializer_objs.save()
 #         return Response(serializer_objs.data)
 #     return Response(serializer_objs.errors)
 # def patch(self,request):
 #     register_objs=Register.objects.get(id=request.data['id'])
 #     serializer_objs=serializer(register_objs,data=request.data,partial=True)
 #     if serializer_objs.is_valid():
 #         serializer_objs.save()
 #         return Response(serializer_objs.data)
 #     return Response(serializer_objs.errors)
 # def delete(self,request):
 #     registero_objs=Register.objects.get(id=request.data['id'])
 #     registero_objs.delete()
 #     return Response("user is deleted")
# @api_view(['GET'])
# def home(request):
#     register_objs=register.objects.all()
#     serializer_objs=serializer(register_objs,many=True)
#     return Response({"status": "200", "payload":  serializer_objs.data})
