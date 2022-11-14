
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('live/', include('liveCalculator.urls')),
    path('p/', include('pratice.urls')),
    path('p1', include('pratice1.urls')),
    path('', include('chatapp.urls')),
]