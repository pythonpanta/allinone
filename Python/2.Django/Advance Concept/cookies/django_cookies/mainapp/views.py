from django.shortcuts import render
from django.http import HttpResponse  
def Home(request):
    return render(request,'mainapp/home.html')
def setcookie(request):
    data=request.GET['userinput']
    print(data)
    response = HttpResponse('cookike set')  
    # response = HttpResponse()  
    response.set_cookie('userinput', data) 
    print(response) 
    #you can set any number of cookie by providing key value pari
    return response 
    # return render(request,'mainapp/setcookie.html') 
 
def getcookie(request):  
    try:
        cookiedata= request.COOKIES['userinput']
    except Exception as e:
        cookiedata='First Enter Text to set Cookie , Then only you can get it'
    # surname = request.COOKIES.get('userinput')   
    # return HttpResponse(cookiedata);  
    return render(request,'mainapp/getcookie.html',{'data':cookiedata})

def deletecookie(request):  
    try:
        response = HttpResponse()
        response.delete_cookie('userinput')
        return response
        # return render(request,'mainapp/home.html')
    except Exception as e:
        cookiedata='First Enter Text to set Cookie , Then only you can get it'
    return render(request,'mainapp/getcookie.html',{'data':cookiedata})
    # surname = request.COOKIES.get('userinput')   
    # return HttpResponse(cookiedata);  

