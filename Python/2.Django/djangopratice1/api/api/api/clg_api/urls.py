
from django.contrib import admin
from django.urls import path
from. import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path("forgot/password", views.ForgorPasswordView.as_view(),
         name='forgot-password'),

    # vendor side

    path("product/create", views.ProductCreateView.as_view(), name='product-create'),
    ###################################################
     path("login", views.LoginView.as_view(), name='login'),
    path("province/list", views.ProvinceListView.as_view(), name='province-list'),
    path("district/list", views.DistrictListView.as_view(), name='district-list'),
    path("municipality/list", views.MunicipalityListView.as_view(),
         name='municipality-list'),
     path("category/list", views.CategoryListView.as_view(),
         name='category-list'),
     path("sub/product/list", views.SubProductListView.as_view(),
         name='sub-product-list'),
         path("product/list", views.ProductListView.as_view(), name='product-list'),
       path("user/register", views.UserRegister.as_view(), name='vendor-signup'),
           path("vendor/register", views.VendorRegister.as_view(), name='vendor-signup'),

    ####################################################################
   
    
    # user side
  
         path("vendor/signup", views.VendorSignupView.as_view(),
         name='vendor-signup'),
  

    path("user/category/list", views.UserCategoryListView.as_view(),
         name='user-category-list'),
   
    path("vendor/product/list", views.VendorProductListView.as_view(),
         name='vendor-product-list'),

    path("order/create", views.OrderCreateView.as_view(), name='order-create'),
    path("otp/generate", views.OtpGenerateListView.as_view(), name='otp-generate'),
    path("each/vendor/list", views.EachVendorListView.as_view(),
         name='each-vendor-list'),


]
