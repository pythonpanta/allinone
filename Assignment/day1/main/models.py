from django.db import models

# Create your models here.
class Stuent(models.Model):
    name=models.CharField(max_length=244)
    roll=models.IntegerField()
    address=models.CharField(max_length=244)
    def __str__(self):
        return self.name

