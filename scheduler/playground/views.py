from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader

def say_hello(request):
    return HttpResponse('hello world')

# def website(request):
#     template = loader.get_template('website.html')
#     return HttpResponse(template.render(request))
