from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('hello world')

def website(request):
    return render(request, 'website.html')

