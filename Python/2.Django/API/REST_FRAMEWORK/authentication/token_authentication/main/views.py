from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import Studentserilaizer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

# Create your views here.
class Student(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=Studentserilaizer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]
    # permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[DjangoModelPermissions]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

