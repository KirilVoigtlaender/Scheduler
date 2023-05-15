
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from .models import Task,Appointment
from .forms import AddTaskForm, AddAppointmentForm

#Test Function
def say_hello(request):
    return HttpResponse('Hello World')

#Test Function
def home(request):
    return render(request, 'home.html')


### MAINVIEW ###
def index(request):
    return render(request, 'index.html')


### TASK ###
def task_list(request):
    return render(request, 'task_list.html', {
        'task_list': Task.objects.all(), 
    })

def add_task(request):
    form = AddTaskForm()
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "TaskListChanged": None,
                        "showMessage": f"{task.name} added."
                    })
                }
            )
    return render(request, 'task_form.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = AddTaskForm(instance=task)
    if request.method == 'POST':
        form = AddTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "TaskListChanged": None,
                        "showMessage": f"{task.name} updated."
                    })
                }
            )
    return render(request, 'task_form.html', {'form': form})

@require_POST
def remove_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "TaskListChanged": None,
                "showMessage": f"{task.name} deleted."
            })
        })
    
    
### APPOINTMENT ###
def appointment_list(request):
    return render(request, 'appointment_list.html', {
        'appointment_list': Appointment.objects.all(),
    })

def add_appointment(request):
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
    return render(request,'appointment_form.html',{
                'form': form
        })
            
def edit_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AddAppointmentForm(instance=appointment)
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
                })
    return render(request, 'appointment_form.html', {'form': form})

@require_POST
def remove_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "AppointmentListChanged": None,
                "showMessage": f"{appointment.name} deleted."
            })
        })