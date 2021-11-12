
from django.urls import path, include
from . import views

urlpatterns = [

    path('signup/', views.Signup, name="signuppage"),
    path('login/', views.Login, name="loginpage"),
    path('logout/', views.Logout, name="logoutpage"),
    path('username/', views.Profile, name="profilepage"),
    path('username/update/', views.Update_profile, name='updatepro'),

] 