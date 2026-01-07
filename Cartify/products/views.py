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

    # Get related products from same category, excluding current product
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:3]

    return render(request, 'products/productdetail.html', {"product": product, "related_products": related_products})