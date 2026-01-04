from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginPage(request):
    print(request.user)

    return render(request, 'users/loginPage.html')

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.user.email)
            return redirect("dashboard")
        else:
            return render(request, 'users/loginPage.html', {'error': 'Invalid credentials'})
    
    return render(request, 'users/loginPage.html')

def logoutUser(request):
    logout(request)
    return redirect("loginPage")

def dashboard(request):

    if request.user.is_anonymous:
        return redirect("loginPage")
    return render(request, 'users/dashboard.html')

def registerUser(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return redirect('home')
    return render(request, 'users/register.html')