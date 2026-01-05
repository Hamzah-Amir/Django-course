from django.urls import path
from users.views import registerUser , loginUser, logoutUser

urlpatterns = [
    path('register', registerUser, name='registerUser'),
    path('login/', loginUser, name='loginUser'),
    path('logout/', logoutUser, name='logout'),
]