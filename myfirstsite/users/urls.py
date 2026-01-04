
from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('login/', views.loginUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
]
