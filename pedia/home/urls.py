from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from home import views



urlpatterns = [
    path('',views.index,name = 'index'),
    # path('signup/',views.signup, name = 'signup'),
    # path("login", views.loginuser, name="login"),
    # path("logout", views.logoutuser, name="logout"),
    # path('social-auth/', include('social_django.urls', namespace="social")),
    path('accounts/', include('allauth.urls')),
    path('index/',views.index),
    path('accounts/profile/',views.index),
    
]
