from rest_framework import serializers
from .models import Student
class Studentserilaizer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','address']