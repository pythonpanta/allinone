from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
class Posts(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=300)
    content=models.TextField()
    timestamp=models.DateField(blank=True)
    img=models.ImageField(upload_to='blog/images')
    slug=models.CharField(max_length=200)

    def __str__(self):
        return self.title +' by '+self.author
    
class BlogComment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(default=now)
    def __str__(self):
        return self.comment[0:15]+"....."+"by "+self.user.username



