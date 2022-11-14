from django.contrib import admin

# Register your models here.
from .models import Hotel,Amenities
admin.site.register(Hotel)
admin.site.register(Amenities)