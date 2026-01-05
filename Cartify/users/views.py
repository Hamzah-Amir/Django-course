from django.shortcuts import render

# Create your views here.
def role(request):
    return render(request, 'users/role.html')

def registerUser(request):
    return  render(request, 'users/register.html')

def loginUser(request):
    return render(request, 'users/login.html')

def logoutUser(request):
    pass
