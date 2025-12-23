from django.shortcuts import render, HttpResponse

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
    return render(request, 'contact.html')
    # return HttpResponse("This is home page")