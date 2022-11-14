from django.shortcuts import render,HttpResponse
from .models import Stuent
from .serializer import studentSerilaizer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
@csrf_exempt
def Home(request,id=None):
    if request.method=='GET':
        if id:
            try:
                stu=Stuent.objects.get(id=id)
            except Exception as e:
                return HttpResponse(f'user with id ={id} is nor found')
            serializer=studentSerilaizer(stu)
        else:
            stu=Stuent.objects.all()
            serializer=studentSerilaizer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=studentSerilaizer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'status':'success'})
        return JsonResponse({'status':'failed'})
    elif request.method=='PUT':
        if id:
            json_data=request.body
            stream=io.BytesIO(json_data)
            python_data=JSONParser().parse(stream)
            serializer=studentSerilaizer(data=python_data)
            stu=Stuent.objects.get(id=id)
            serializer=studentSerilaizer(stu,data=python_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'status':'success'})
            return JsonResponse({'status':'failed'})
      
        return HttpResponse('provide the id for updating data')
    elif request.method=='DELETE':
        if id:
            data=Stuent.objects.get(id=id)
            data.delete()
            return JsonResponse({'status':'success'})
        return JsonResponse({'status':'failed','message':'id not found'})
    else:
        return JsonResponse({'message':'error'})
      



