from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import*
from .models import*
from rest_framework.response import Response
# Create your views here.


class owner(APIView):
    def get(self, request, format=None):
        owner_ob = owner.objects.all()
        serializer_ob = serializers(owner_ob, many=True)
        return Response({"status": "200", "payload":  serializer_ob.data})

    def post(self, request, format=None):
        serializer_ob = serializers(data=request.data)
        if serializer_ob.is_valid():
            serializer_ob.save()
            return Response({"status": "200", "payload":  serializer_ob.data})
        return Response({"status": "400", "message": serializer_ob.errors})