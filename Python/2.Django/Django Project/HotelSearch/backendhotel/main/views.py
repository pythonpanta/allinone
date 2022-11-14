from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .models import Hotel
class Home(View):
    def get(self,request):
        hotelsobj=Hotel.objects.all()
        print(request.GET.get('sort_by'))
        if request.GET.get('sort_by'):
            sort_by_value=request.GET.get('sort_by')
            if sort_by_value=='asc':
                hotelsobj=hotelsobj.order_by('price')
            elif sort_by_value=='dsc':
                hotelsobj=hotelsobj.order_by('-price')
        if request.GET.get('amount'):
            amount=request.GET.get('amount')
            hotelsobj=hotelsobj.filter(price__lte=amount)
            

        

        payload=[]
        for hotel in hotelsobj:
            payload.append(
                {'hotel_name':hotel.name,
                'hotel_price':hotel.price,
                'hotel_des':hotel.des,
                'hotel_img':str(hotel.img)}
            )
        return JsonResponse(payload,safe=False)

