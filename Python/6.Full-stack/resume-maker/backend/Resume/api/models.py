from pyexpat import model
from tokenize import blank_re
from django.db import models

class ClinetData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField(auto_now_add=False,auto_now=False)
    gender=models.CharField(max_length=10)
    location=models.CharField(max_length=100)
    uimage=models.ImageField(upload_to='media/client',blank=True)
    about=models.TextField()
    skills=models.TextField()
    experience=models.TextField()
    education=models.TextField()

