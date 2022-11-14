from django.db import models

class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=300)
    phone=models.CharField(max_length=300)
    email=models.CharField(max_length=300)
    content=models.TextField()
    timestamp=models.DateField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'message from'+self.name
    

