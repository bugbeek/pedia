from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from home import views



urlpatterns = [
    path('',views.index,name = 'index'),
    path('accounts/', include('allauth.urls')),
    path('index/',views.index),
    path('profiledetail/',views.profiledetail),
    path('accounts/profile/',views.index),
    path('search/', views.search, name= 'search'),
    path('userbio/', views.userbio),
] 
