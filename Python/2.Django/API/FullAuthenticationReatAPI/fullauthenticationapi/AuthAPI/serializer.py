from django.forms import ValidationError
from rest_framework import serializers
from . models import User
class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input-type':'password'},write_only=True)
    class Meta:
        model=User
        fields=['id','username','email','tc','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def validate(self,attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password !=password2:
            raise ValidationError('Password and confirm Password doesnot match')
        return attrs
    def create(self,validate_data):
        return User.objects.create_user(**validate_data)   

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password']

        
    def validate(self,attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        print(email,password)
        if not  User.objects.filter(email=email,password=password).exists():
            raise ValidationError('User with email and password  doesnot match')
        return attrs
