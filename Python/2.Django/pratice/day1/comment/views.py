from django.shortcuts import render,redirect
from . models import Blog,Comment
# Create your views here.
def Home(request):
    blog=Blog.objects.all()
    context={'blogs':blog}
    return render(request,'comment/home.html',context)
def BlogDetail(request,id):
    comments=Comment.objects.filter(blog_id=id)
    blog=Blog.objects.get(id=id)
    return render(request,'comment/blogdetails.html',{'comments':comments,'blog':blog})
def postcomment(request,id):
    comments=Comment.objects.filter(blog_id=id)
    blog=Blog.objects.get(id=id)
    data=request.GET['comment-data']
    Comment(user=request.user,blog=blog,comment=data).save()
    return render(request,'comment/blogdetails.html',{'comments':comments,'blog':blog})
