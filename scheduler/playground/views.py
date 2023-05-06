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

def say_hello(request):
    return HttpResponse('hello world')

def website(request):
    time_records = TimeRecord.objects.all()
    week = timezone.now().isocalendar()[1]
    current_records = [time_record for time_record in time_records if time_record.get_week() == week]
    if request.method == 'POST':
        weekrequest = request.POST['weekrequest']

        if weekrequest == 'next-week':
            current_records = [time_record for time_record in time_records if
                               time_record.get_week() == week + 1]
        if weekrequest == 'last-week':
            current_records = [time_record for time_record in time_records if
                               time_record.get_week() == week - 1]
    current_week = CalendarWeek(year=current_records[0].get_year(), week=current_records[0].get_week())

    sunday = Appointment.objects.filter(date=current_week[0]).values()
    monday = Appointment.objects.filter(date=current_week[1]).values()
    tuesday = Appointment.objects.filter(date=current_week[2]).values()
    wednesday = Appointment.objects.filter(date=current_week[3]).values()
    thursday = Appointment.objects.filter(date=current_week[4]).values()
    friday = Appointment.objects.filter(date=current_week[5]).values()
    saturday = Appointment.objects.filter(date=current_week[6]).values()




    template = loader.get_template('website.html')
    context = {
        'sunday': sunday,
        'monday': monday,
        'tuesday': tuesday,
        'wednesday': wednesday,
        'thursday': thursday,
        'friday': friday,
        'saturday': saturday,
        'currentday' : current_records[0].get_week(),
        'date1' : current_week[0],
        'date2' : current_week[1],
        'date3' : current_week[2],
        'date4' : current_week[3],
        'date5' : current_week[4],
        'date6' : current_week[5],
        'date7' : current_week[6],
    }
    return HttpResponse(template.render(context, request))

