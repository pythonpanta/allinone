from django.contrib import admin
from . models import Order, Product, Province, District, Category, SubCategory,Municipality

# Register your models here.
@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display=['id','name']

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display=['id','name','province_id' ]

@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    list_display=['id','name','province_id','district_id' ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name' ]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','category' ]

admin.site.register(Product)
admin.site.register(Order)
