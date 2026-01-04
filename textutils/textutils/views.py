from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is the index page of TextUtils.")

def removepunctuation(request):
    return HttpResponse("This is the Remove Punctuation page.")

def capitalizefirst(request):
    return HttpResponse("This is the Capitalize First Letter page.")

def removespaces(request):
    return HttpResponse("This is the Remove Extra Spaces page.")

def charcount(request):
    return HttpResponse("This is the Character Count page.")