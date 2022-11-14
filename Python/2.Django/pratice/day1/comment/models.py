from django.db import models
from django.contrib.auth.models import User
class Blog(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    author=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='blog/',blank=True)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title[:30]+'...'+'by'+'['+self.author+']'
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    time=models.DateTimeField(auto_now=True)
    comment=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

