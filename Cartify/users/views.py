from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def role(request):
    return render(request, 'users/role.html')

def registerUser(request):

    # Writing backend of authentication
    role = request.GET.get('role') if request.method == 'GET' else request.POST.get('role')
    if not role:
        return redirect('role')
    
    if request.method == 'GET':
        return render(request, 'users/register.html', {'role': role})
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        user = CustomUser.objects.create_user(username=username,
                                               email=email,
                                               first_name=first_name,
                                               last_name=last_name,
                                               password=password,
                                               role=role,
                                               gender=gender,
                                               age=age,
                                               phone_number=phone)
        user.save()
        return redirect('loginUser')

    return redirect('role')

def loginUser(request):
    return render(request, 'users/login.html')

def logoutUser(request):
    pass
