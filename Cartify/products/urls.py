from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login', home, name='loginUser'),
    path('register', home, name='registerUser'),
]
