from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('register', views.register, name = 'register'),
    path('signout', views.signout, name = 'signout'),
    
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    
    path('success_register/', views.success_register, name='success_register'),
    path('profile/', views.profile, name='user_profile'),
    
    #Forgot password
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'home/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'home/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'home/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'home/password_reset_complete.html'),name='password_reset_complete'),
]
