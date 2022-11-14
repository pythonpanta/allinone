from django.urls import path
from . import views
urlpatterns = [
    path('data/',views.Resume.as_view(),name='post_data'),

]