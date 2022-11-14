from django.contrib import admin
from home.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phone','email','timestamp']
admin.site.register(Contact,ContactAdmin)
