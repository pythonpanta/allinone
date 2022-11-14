from django.shortcuts import render

def PHome(request):
    print('pHome')
    return render(request,'pratice1/index.html')
