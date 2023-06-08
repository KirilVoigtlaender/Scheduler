
import json
from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

from django.template import loader
from .models import Task,Appointment,PersonalPreference
from .forms import AddTaskForm, AddAppointmentForm,AddPersonalPreferencesForm

from datetime import date
from calendarweek import CalendarWeek
from datetime import timedelta

from .algorithm import algorithm
from .repition import reptition

def index(request):
    #main view with the button
    return render(request, 'index.html')#The same as his index.html



## TASK ##
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
    form = AddTaskForm(instance=task)  # Define an empty form instance
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

@ require_POST
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


## APPOINTMENT ##
def appointment_list(request):
    return render(request, 'appointment_list.html', {
        'appointment_list': Appointment.objects.all(), # Update the key to 'appointment_list'
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
    form = AddAppointmentForm(instance=appointment)  # Define an empty form instance
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

@ require_POST
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



##PersonalPrefernces ##
def personalpreference_list(request):
    return render(request, 'personalpreference_list.html', {
        'personalpreference_list': PersonalPreference.objects.all(),  # Update the key to 'personalpreferences_list'
    })

def add_personalpreference(request):
    form = AddPersonalPreferencesForm()
    if request.method == "POST":
        form = AddPersonalPreferencesForm(request.POST)
        if form.is_valid():
            personalpreference = form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "PersonalPreferenceListChanged": None,
                        "showMessage": f"{personalpreference.name} added."
                    })
                }
            )
    return render(request, 'personalpreference_form.html', {'form': form})

def edit_personalpreference(request, pk):
    personalpreference = get_object_or_404(PersonalPreference, pk=pk)
    form = AddPersonalPreferencesForm(instance=personalpreference)  # Define an empty form instance
    if request.method == 'POST':
        form = AddPersonalPreferencesForm(request.POST, instance=personalpreference)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "PersonalPreferenceListChanged": None,
                        "showMessage": f"{personalpreference.name} updated."
                    })
                }
            )
    return render(request, 'personalpreference_form.html', {'form': form})

@ require_POST
def remove_personalpreference(request, pk):
    personalpreference = get_object_or_404(PersonalPreference, pk=pk)
    personalpreference.delete()
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "PersonalPreferenceListChanged": None,
                "showMessage": f"{personalpreference.name} deleted."
            })
        })

## SCHEDULE ##
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
        
    to_appointment = reptition()
    to_schedule = algorithm(to_appointment, current_week[0])
    monday = Appointment.objects.filter(date=current_week[0]).values() 
    tuesday = Appointment.objects.filter(date=current_week[1]).values() 
    wednesday = Appointment.objects.filter(date=current_week[2]).values() 
    thursday = Appointment.objects.filter(date=current_week[3]).values() 
    friday = Appointment.objects.filter(date=current_week[4]).values() 
    saturday = Appointment.objects.filter(date=current_week[5]).values() 
    sunday = Appointment.objects.filter(date=current_week[6]).values() 

    mondaytasks = []
    for task in to_schedule:
        if task.date == current_week[0]:
            mondaytasks.append(task)
    tuesdaytasks = []
    for task in to_schedule:
        if task.date == current_week[1]:
            tuesdaytasks.append(task)
    wednesdaytasks = []
    for task in to_schedule:
        if task.date == current_week[2]:
           wednesdaytasks.append(task)
    thursdaytasks =[]
    for task in to_schedule:
        if task.date == current_week[3]:
            thursdaytasks.append(task)
    fridaytasks = []
    for task in to_schedule:
        if task.date == current_week[4]:
            fridaytasks.append(task)
    saturdaytasks = []
    for task in to_schedule:
        if task.date == current_week[5]:
            saturdaytasks.append(task)
    sundaytasks = []
    for task in to_schedule:
        if task.date == current_week[6]:
            sundaytasks.append(task)

    
    mondayappointment = []
    for appointment in to_appointment:
        if appointment.date == current_week[0]:
            mondayappointment.append(appointment)
    tuesdayappointment = []
    for appointment in to_appointment:
        if appointment.date == current_week[1]:
            tuesdayappointment.append(appointment)
    wednesdayappointment = []
    for appointment in to_appointment:
        if appointment.date == current_week[2]:
           wednesdayappointment.append(appointment)
    thursdayappointment =[]
    for appointment in to_appointment:
        if appointment.date == current_week[3]:
            thursdayappointment.append(appointment)
    fridayappointment = []
    for appointment in to_appointment:
        if appointment.date == current_week[4]:
            fridayappointment.append(appointment)
    saturdayappointment = []
    for appointment in to_appointment:
        if appointment.date == current_week[5]:
            saturdayappointment.append(appointment)
    sundayappointment = []
    for appointment in to_appointment:
        if appointment.date == current_week[6]:
            sundayappointment.append(appointment)


    template = loader.get_template('website.html')
    context = {
        'monday': monday, 
        'mondaytasks' : mondaytasks,
        'tuesday': tuesday,
        'tuesdaytasks': tuesdaytasks,
        'wednesday': wednesday,
        'wednesdaytasks': wednesdaytasks,
        'thursday': thursday,
        'thursdaytasks': thursdaytasks,
        'friday': friday,
        'fridaytasks': fridaytasks,
        'saturday': saturday,
        'saturdaytasks': saturdaytasks,
        'sunday': sunday,
        'sundaytasks': sundaytasks,
        'mondayappointment': mondayappointment,
        'tuesdayappointment': tuesdayappointment,
        'wednesdayappointment': wednesdayappointment, 
        'thursdayappointment': thursdayappointment,
        'fridayappointment': fridayappointment,
        'saturdayappointment': saturdayappointment,
        'sundayappointment': sundayappointment,
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

