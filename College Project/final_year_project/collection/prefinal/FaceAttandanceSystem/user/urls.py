from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import MyPasswordChange,MyPasswordResetForm,MySetPasswordForm
urlpatterns = [
    path('login/',views.Login,name='Login'),
    path('register/',views.Register,name='Register'),
    path('logout/',views.Logout,name='Logout'),

    # for changing the password
    path('changepass/',auth_views.PasswordChangeView.as_view(template_name='user/changepassword.html',form_class=MyPasswordChange,success_url='/user/changepassdone/'), name='Changepassword'),
    path('changepassdone/',auth_views.PasswordChangeDoneView.as_view(template_name='user/resultpasswordchange.html'), name='passwordchangedone'),
    # for resetting the password 
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='user/passwordreset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='user/passwordresetdone.html'),name='password_reset_done'),
    path('password_reset_Conform/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='user/passwordresetconfirm.html',form_class =MySetPasswordForm),name='password_reset_confirm'),
    path('password_reset_Complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/passwordresetcomplete.html'),name='password_reset_complete'), 

]
