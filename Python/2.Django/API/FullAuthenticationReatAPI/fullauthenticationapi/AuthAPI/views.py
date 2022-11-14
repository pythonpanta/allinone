from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializer import RegisterSerializer,LoginSerializer
from rest_framework import status
from django.contrib.auth import authenticate

from AuthAPI import serializer
# Create your views here.
class UserRegister(APIView):
    def post(self,request):
        try:
            data=request.data
            serilaizer=RegisterSerializer(data=data)
            if serilaizer.is_valid():
                serilaizer.save()
                return Response({'msz':'User is successfully Created'},status=status.HTTP_201_CREATED)
            return Response({'error':serilaizer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':'user is not register'},status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    def post(self,request):
        try:
            data=request.data
            serilaizer=LoginSerializer(data=data)
            if serilaizer.is_valid():
                print(serializer.data)
                email=serializer.data.get('email')
                password=serializer.data.get('password')
                user=authenticate(email=email,password=password)
                if user is not None:
                    return Response({'msz':'User is successfully Login'},status=status.HTTP_201_CREATED)
            return Response({'error':serilaizer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'error':'user is not Login'},status=status.HTTP_400_BAD_REQUEST)
