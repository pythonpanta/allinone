from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from blog.models import Posts
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
def home(request):
    allpost=Posts.objects.all()
    context={'allpost':allpost}
    return render(request,'home/home.htm',context)
def about(request):
    return render(request,'home/about.htm')
  
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        content = request.POST.get('content', '')
        contacts = Contact(name=name, email=email, phone=phone, content=contact)
        contacts.save()
        messages.success(request, "Your form's is successfully send. ")
    return render(request,'home/contact.htm')  
def search(request):
    query=request.GET['query']
    allpost=Posts.objects.filter(title__icontains=query)
    params={'allpost':allpost}
    return render(request,'home/search.htm',params)     

def handlesignup(request):
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        #check the authentication
        if len(username)>10:
            messages.error(request,'username must be greater than 10')
            return redirect("home")
        # if not  username.alnum:
        #         #messages.error(request,'username must be greater than 10)
        #     return redirect("home")    
        if pass1 != pass2:
            messages.error(request, 'Password does not match')
            return redirect("home")   
        #create the user
        print(username,fname,lname,pass1)
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request, 'Your account have been successfully created')
        return redirect("home")
    
    else:
        return HttpResponse("ERROR:404")

def handlelogin(request):
    if request.method=="POST":
        username=request.POST['loginusername']
        password=request.POST['pass']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print("successfully login")
            messages.success(request, 'you have login in the website')
            return redirect("home")
        else:
            print("enter the correct user name and the password")
            messages.error(request, 'Enter the correct username and the password')
    return HttpResponse("Error _404")
def handlelogout(request):
    logout(request)
    print("account is logout successfully")
    messages.success(request, 'Now you are logout successfully')
    return redirect("home")
      

