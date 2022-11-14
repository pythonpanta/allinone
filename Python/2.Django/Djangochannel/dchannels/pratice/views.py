from django.shortcuts import render,HttpResponse

def Home(request):
    print('python')
    return render(request,'pratice/index.html')



