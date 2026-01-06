from django.shortcuts import render
from products.models import Product

# Create your views here.

def home(request):
    # Logic for Fetching Products
    products = Product.objects.filter(stock__gt=0)

    return render(request, 'products/home.html', {"products": products})

def productDetail(request, uuid):
    id = uuid
    product = Product.objects.filter(id=id).first()
    print(product)

    return render(request, 'products/productdetail.html', {"product": product})