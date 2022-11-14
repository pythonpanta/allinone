from django.db import models
class Amenities(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Hotel(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    des=models.TextField()
    image=models.ImageField(upload_to='hotel',blank=True)
    amenities=models.ManyToManyField(Amenities)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def get_amenities(self):
        payload=[]
        for amenity in self.amenities.all():
            payload.append({
                'id':amenity.id,
                'name':amenity.name
            })
        return payload


    def __str__(self):
        return self.name




