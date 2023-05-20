from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Appointment
from datetime import date
from django.db import models
from calendarweek import CalendarWeek
from django.db import models
from .models import TimeRecord
from django.utils import timezone
from datetime import timedelta
from asgiref.sync import sync_to_async

def say_hello(request):
    return HttpResponse('hello world')

def website(request):
    day = request.session.get('current_week', date.today().isoformat())
    if request.method == 'POST':
        weekrequest = request.POST['weekrequest']

        if weekrequest == 'next-week':
            day = (date.fromisoformat(day) + timedelta(0,0,0,0,0,0,1)).isoformat()
        if weekrequest == 'last-week':
            day = (date.fromisoformat(day) - timedelta(0,0,0,0,0,0,1)).isoformat()
    
    current_week = CalendarWeek().from_date(date.fromisoformat(day))
    request.session['current_week'] = day

    monday = Appointment.objects.filter(date=current_week[0]).values()
    tuesday = Appointment.objects.filter(date=current_week[1]).values()
    wednesday = Appointment.objects.filter(date=current_week[2]).values()
    thursday = Appointment.objects.filter(date=current_week[3]).values()
    friday = Appointment.objects.filter(date=current_week[4]).values()
    saturday = Appointment.objects.filter(date=current_week[5]).values()
    sunday = Appointment.objects.filter(date=current_week[6]).values()




    template = loader.get_template('website.html')
    context = {
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        'sunday': sunday,
        'currentday' : date.today(),
        'date1' : current_week[0],
        'date2' : current_week[1],
        'date3' : current_week[2],
        'date4' : current_week[3],
        'date5' : current_week[4],
        'date6' : current_week[5],
        'date7' : current_week[6],
    }

    

    return HttpResponse(template.render(context, request))

