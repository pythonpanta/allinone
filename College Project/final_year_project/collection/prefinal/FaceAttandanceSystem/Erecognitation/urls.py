from django.urls import path
from . import views
urlpatterns = [
    path('',views.Home,name='Home'),
    path('dashboard/',views.DashBoard,name='DashBoard'),
    path('attandance_in/',views.Attandance_IN,name='Attandance_IN'),
    path('attandance_out/',views.Attandance_OUT,name='Attandance_OUT'),
    path('view_attendance/',views.View_Attendance,name='View_Attendance'),
    path('train_system/',views.Trainsystem,name='Trainsystem'),
    path('add-photo/',views.Addphoto,name='Addphoto'),
    path('view-report/',views.Viewreport,name='Viewreport'),


]