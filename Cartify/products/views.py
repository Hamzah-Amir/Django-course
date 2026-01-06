from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'products/home.html')

def productDetail(request):
    if request.method == "GET":
        uid = request.method.GET.get('uuid')
    return render(request, 'products/productdetail.html')