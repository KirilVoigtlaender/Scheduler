from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Event

def say_hello(request):
    return HttpResponse('Hello World')

def index(request):
    #main view with the button
    return render(request, 'playground/base.html')

def home(request):
    return render(request, 'playground/home.html')

def add_task():
    #when add_task button get clicked
    return

def add_movie(request):
    form = AddTaskForm()
    return render(request, 'task_form.html', {
        'form': form,
    })

def add_appointment():
    #when add_appontment button get clicked
    return

def add_repition():
    #when reppition button is clicked
    return

def say_Task(request):
    return HttpResponse('Add a Task')

def say_Appointment(request):
    return HttpResponse('Add an Appointment')

def say_():
    return
