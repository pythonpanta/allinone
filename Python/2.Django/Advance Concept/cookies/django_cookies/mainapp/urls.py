from django.urls import path
from . import views
urlpatterns=[
    path('',views.Home,name='Home'),
    path('setcookie/',views.setcookie,name='setcookie'),
    path('getcookie/',views.getcookie,name='getcookie'),
    path('deletecookie/',views.deletecookie,name='deletecookie'),
    ]