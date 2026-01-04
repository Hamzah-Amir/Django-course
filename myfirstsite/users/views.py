from django.shortcuts import render

# Create your views here.

def loginPage(request):
    return render(request, 'users/loginPage.html')

def loginUser(request):
    pass

def logoutUser(request):
    pass