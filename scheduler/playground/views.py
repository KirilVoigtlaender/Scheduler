from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Appointment
from django.db import models

def say_hello(request):
    return HttpResponse('hello world')

def website(request):
    appointments = Appointment.objects.all().values
    template = loader.get_template('website.html')
    context = {
        'appointments': appointments,
        'date': models.DateField('2023-07-20'),
    }
    return HttpResponse(template.render(context, request))

