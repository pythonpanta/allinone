from rest_framework import serializers
from . models import ClinetData
class ClientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClinetData
        fields=['name','email','dob','gender','location','uimage','about','skills','education','experience']
