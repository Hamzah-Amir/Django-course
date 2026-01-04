from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginPage(request):
    print(request.user)

    return render(request, 'users/loginPage.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.email)
            return render(request, "users/dashboard.html")
        else:
            return render(request, 'users/loginPage.html', {'error': 'Invalid credentials'})
    
    return render(request, 'users/loginPage.html')

def logoutUser(request):
    logout(request)
    return redirect("loginPage")