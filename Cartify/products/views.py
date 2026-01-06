from django.shortcuts import render
from products.models import Product

# Create your views here.

def home(request):
    # Logic for Fetching Products
    products = Product.objects.filter(stock__gt=0)
            
    return render(request, 'products/home.html', {"products": products})

def productDetail(request):
    if request.method == "GET":
        uid = request.method.GET.get('uuid')
    return render(request, 'products/productdetail.html')