from django.urls import path
from . import views
urlpatterns=[
    path('student/',views.Home,name='home'),
    path('student/<int:id>',views.Home,name='home'),
]