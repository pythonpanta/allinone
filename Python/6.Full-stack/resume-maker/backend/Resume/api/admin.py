from django.contrib import admin
from . models import ClinetData
@admin.register(ClinetData)
class CliemtDataAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','gender','location','uimage','about','skills','education','experience']
