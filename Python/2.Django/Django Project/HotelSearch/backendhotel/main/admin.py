from django.contrib import admin

from .models import Hotel,HotelFeatures
class HotelFeaturesAdmin(admin.ModelAdmin):
    list_display=['id','name','created_date','updated_date']
admin.site.register(HotelFeatures,HotelFeaturesAdmin)


class HotelAdmin(admin.ModelAdmin):
    list_display=['id','name','price','des','image_tag','created_date','updated_date']
admin.site.register(Hotel,HotelAdmin)

