from django.shortcuts import render
def Home(request,group_name):
    context={'gn':group_name}
    return render(request,'chat/index.html',context)
