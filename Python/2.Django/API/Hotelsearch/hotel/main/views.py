from django.shortcuts import render
from django.http import JsonResponse
from .models import Hotel,Amenities
def Home(request):
    return render(request,'main/index.html')
def get_hotel(request):
    try:
        if request.GET.get('price'):
            price=request.GET.get('price')
            hotels=Hotel.objects.filter(price__lte=price)
        elif request.GET.get('amenities'):
            price=request.GET.get('amenities')
            data=price.split(',')
            am=[]
            for a in data:
                am.append(int(a))
            hotels=Hotel.objects.filter(amenities__id__in=am).distinct()
        elif request.GET.get('sort_by'):
            data=request.GET.get('sort_by')
            if data=='asc':
                hotels=Hotel.objects.order_by('price')
            elif data=='dsc':
                hotels=Hotel.objects.order_by('-price')
        else:
            hotels=Hotel.objects.all()
        payload=[]
        for hotel in hotels:
            payload.append({
                'id':hotel.id,
                'name':hotel.name,
                'price':hotel.price,
                'des':hotel.des,
                'image':str(hotel.image),
                'amenities':str(hotel.get_amenities())
            })
        return JsonResponse({'data':payload},safe=False)
    except Exception as e:
        print(e)
        return JsonResponse({'message':str(e)},safe=False)
def get_amenities(request):
    try:
        data=Amenities.objects.all()
        payload=[]
        for amenity in data:
            payload.append({
                'id':amenity.id,
                'name':amenity.name
            })
        return JsonResponse({'message':'ok','data':payload})
    except Exception as e:
        return JsonResponse({'message':str(e)})

    