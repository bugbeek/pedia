from django.contrib import admin
from django.urls import path
from home import views



urlpatterns = [
    path('',views.index,name = 'index'),
    path('signup/',views.signup, name = 'signup'),
    path("login", views.loginuser, name="login"),
    path("logout", views.logoutuser, name="logout"),
]
