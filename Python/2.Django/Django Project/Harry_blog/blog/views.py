from django.shortcuts import render,redirect
from blog.models import Posts,BlogComment
from django.contrib.auth.models import User
from django.contrib import messages
from blog.templatetags import extras
def bloghome(request):
    allpost= Posts.objects.all()
    context={'allpost':allpost}
    return render(request,'blog/home.htm',context)
def blogpost(request,slug):
    post= Posts.objects.filter(slug=slug).first()
    comment= BlogComment.objects.filter(post=post,parent=None)
    replies= BlogComment.objects.filter(post=post).exclude(parent=None)
    repDic={}
    for reply in replies:
        if reply.parent.sno not in repDic.keys():
            repDic[reply.parent.sno]=[reply]
        else:
            repDic[reply.parent.sno].append(reply)
    
    context={'post':post,'comment':comment,'user':request.user,'replyDict':repDic}
    return render(request,'blog/blogpost.htm',context)
def postcomment(request):
    if request.method=="POST":
        comment=request.POST.get("comment")
        user=request.user
        postno=request.POST.get("postno")
        post=Posts.objects.get(sno=postno)
        parentsno=request.POST.get("parentsno")
        if parentsno==" ":
            comments=BlogComment(comment=comment,post=post,user=user)
            comments.save()
            messages.success(request, 'your Comment has been  posted successfully')  
        else:
            parent=BlogComment.objects.get(sno=parentsno)
            comments=BlogComment(comment=comment,post=post,user=user,parent=parent)  
            comments.save()
            messages.success(request, 'your Reply has been  posted successfully')    
       
          
    return redirect(f"/blog/{post.slug}")   

      