
import json
from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from django.template import loader
from .models import Task,Appointment
from .forms import AddTaskForm, AddAppointmentForm

def say_hello(request):
    return HttpResponse('Hello World')

def index(request):
    #main view with the button
    return render(request, 'index.html')#The same as his index.html
#Don't know if we need this function for now
def home(request):
    return render(request, 'home.html')

def task_list(request):
    return render(request, 'task_list.html', {
        'task_list': Task.objects.all(),  # Update the key to 'task_list'
    })



def add_task(request):
    form = AddTaskForm()
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return HttpResponse(
                status = 204,
                headers={
                    'HX-Trigger': json.dumps({
                        "TaskListChanged":None,
                        "showMessage": f"{task.name} added."
                    })
                })
        else:
            form = AddTaskForm()
    return render(request,'task_form.html', {
                'form': form,
    })

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status = 204,
                headers={
                'HX-Trigger': json.dumps({
                    "showMessage": f"{task.name} updated."
                    })
            })
        else:
            form = AddTaskForm(instance=task)
        return render(request, 'task_form.html', {
        'form': form,
        'task': task,
    })

@ require_POST
def remove_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "showMessage": f"{task.name} deleted."
            })
        })

def appointment_list(request):
    return render(request, 'appointment_list.html', {
        'appointment_list': Appointment.objects.all(),
    })

def add_appointment(request):
    #when add_appontment button get clicked
    form = AddAppointmentForm()
    if request.method == "POST":
        form = AddAppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return HttpResponse(
                status = 204,
                headers={
                     'HX-Trigger': json.dumps({
                        "AppointmentListChanged": None,
                        "showMessage": f"{appointment.name} added."
                    })
                })
        else:
            form = AddAppointmentForm()
    return render(request,'appointment_form.html',{
                'form': form,
        })
            



def edit_appointment(request, pk):
     appointment = get_object_or_404(Appointment, pk=pk)
     if request.method == "POST":
         form= AddAppointmentForm(request.POST, instance=appointment)
         if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "AppointmentListChanged": None,
                        "showMessage": f"{appointment.name} updated."
                    })
                }
            )
         else:
             form = AddAppointmentForm(instance=appointment)
             return render(request, 'appointment_form.html', {
        'form': form,
        'appointment': appointment,
    })



@ require_POST
def remove_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "movieListChanged": None,
                "showMessage": f"{appointment.name} deleted."
            })
        })




