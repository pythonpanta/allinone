from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('DashBoard')
        else:
            messages.warning(request,'Login failed ! Please Enter Correct Credential ')

        
    return render(request,'user/login.html')


@login_required
def Register(request):
    if request.method=='POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get("password1")
        pass2 = request.POST.get("password2")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        
        checkuser = User.objects.filter(username=username)
        checkemail = User.objects.filter(email=email)
        if username=='' and email=='' and pass1=='' and  pass2=='' and fname=='' and lname=='':
            messages.warning(request, "Required All field.")
            return render(request, 'user/register.html')
        if checkemail:
            messages.warning(request, "Email already exist....Enter Unique One")
            return render(request, 'user/register.html')
        elif checkuser:
            messages.warning(request, "User With this name is already exist. Please Enter Unique Username....")
            return render(request, 'user/register.html')
        elif pass1!=pass2:
            messages.warning(request, "Password and Confirm password did not match .")
            return render(request, 'user/register.html')
        user = User.objects.create_user(username=username, email=email,
                                            password=pass1)
        user.first_name=fname
        user.last_name=lname
        user.save()
        messages.success(request, "Congratulation , successfully Register!!")
        
    return render(request,'user/register.html')
@login_required
def Logout(request):
    logout(request)
    return redirect('/')


