from rest_framework import serializers
from . models import Stuent
class studentSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Stuent
        fields='__all__'
