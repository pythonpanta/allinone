from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    #API for the comments
    path('postcomment',views.postcomment,name='postcomment'),
    path('',views.bloghome,name='bloghome'),
    path('<str:slug>',views.blogpost,name='blogpost'),

    

]