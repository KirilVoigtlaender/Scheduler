from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Appointment
from datetime import date
from django.db import models

def say_hello(request):
    return HttpResponse('hello world')

def website(request):
    sunday = Appointment.objects.filter(date='2023-07-14').values()
    monday = Appointment.objects.filter(date='2023-07-15').values()
    tuesday = Appointment.objects.filter(date='2023-07-16').values()
    wednesday = Appointment.objects.filter(date='2023-07-17').values()
    thursday = Appointment.objects.filter(date='2023-07-18').values()
    friday = Appointment.objects.filter(date='2023-07-19').values()
    saturday = Appointment.objects.filter(date='2023-07-20').values()
    template = loader.get_template('website.html')
    context = {
        'sunday': sunday,
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        # 'date1' : models.DateField(default=date.today),
        # 'date2' : models.DateField(default=date.today+1),
        # 'date3' : models.DateField(default=date.today+2),
        # 'date4' : models.DateField(default=date.today+3),
        # 'date5' : models.DateField(default=date.today+4),
        # 'date6' : models.DateField(default=date.today+5),
        # 'date7' : models.DateField(default=date.today+6),
    }
    return HttpResponse(template.render(context, request))

