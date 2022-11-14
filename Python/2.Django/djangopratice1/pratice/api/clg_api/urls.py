
from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path("district/list/", views.DistrictListView.as_view(), name='district-list'),
    path("province/list/", views.ProvinceListView.as_view(), name='province-list'),
    path("municipality/list/", views.MunicipalityListView.as_view(),
         name='municipality-list'),
    path("category/list/", views.CategoryListView.as_view(),
         name='category-list'),
     path("sub/product/list/", views.SubProductListView.as_view(),
         name='sub-product-list/'),
    path("product/list/", views.ProductListView.as_view(), name='product-list'),
    path("user/register/", views.UserRegister.as_view(), name='vendor-signup'),
    path("vendor/register/", views.VendorRegister.as_view(), name='vendor-signup'),
]