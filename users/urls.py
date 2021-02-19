from django.urls import path, include

from . import views

from django.contrib.auth import views as auth_views

app_name = 'users'
#localhost:8000/users/

urlpatterns = [
    path('loginpage/', views.loginpage, name='loginpage'),
    path('signup/', views.signup, name='signup'),
    path('signupProcess/', views.signup_process, name='signup_process'),
    path('loginProcess/', views.login_process, name='login_process'),
    path('logout/', views.logout, name='logout'),
    path('findpassword/', views.findpassword, name='findpassword'),
    path('findid/', views.findid, name='findid'),
    path('modify/', views.modify, name='modify'),
    path('modifyProcess/', views.modifyprocess, name='modifyprocess'),
    path('withdrawl/', views.withdrawl, name='withdrawl'),
    path('withdrawlProcess/', views.withdrawlprocess, name='withdrawlprocess'),


]
