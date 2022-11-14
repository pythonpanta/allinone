from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('get_hotel/',views.get_hotel),
    path('get_amenities/',views.get_amenities),
    ]

