from django.shortcuts import render

# Create your views here.

def seller(request):
    return render(request, 'seller/seller_dashboard.html')