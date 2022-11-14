from django.contrib import admin
from blog.models import Posts,BlogComment
admin.site.register((Posts,BlogComment))
