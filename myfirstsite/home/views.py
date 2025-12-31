from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contact

# Create your views here.

def home(request):
    context = {
        'name': 'Hamza'
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is home page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        date = datetime.today()
        contact = Contact(name=name, email=email, phone=number, message=message, date=date)
        contact.save()

    return render(request, 'contact.html')
    # return HttpResponse("This is home page")