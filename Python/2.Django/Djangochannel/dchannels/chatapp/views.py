from django.shortcuts import render
def Chat(request):
    return render(request,'chatapp/index.html')
