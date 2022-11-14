from django.db import models
from django.utils.safestring import mark_safe

class HotelFeatures(models.Model):
    name=models.CharField(max_length=100)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name


#  ""
class Hotel(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()                          
    des=models.TextField()
    img=models.ImageField(upload_to='hotelimage',null=True)
    features=models.ManyToManyField(HotelFeatures)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name

    def image_tag(self):
        return mark_safe(f"<img src={self.img.url} height='40' width='40'/>")

