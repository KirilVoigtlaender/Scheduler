#These are the functions for the database, which is programmed in models

from .models import Task, Appointment

def add_task(name, expected_time, date, importancy_level):
    return Task.objects.create(name=name, date=date, expected_time=expected_time, importancy_level=importancy_level)

def add_appointment(name,start_time, end_time, date, repetition ):
    return Appointment.objects.create(name = name, start_time=start_time, end_time=end_time, repetition=repetition)

def delete_task(task_id):
    try:
        task = Task.objects.get(pk=task_id)
        task.delete()
        return True
    except Task.DoesNotExist:
        return False

def delete_appointment(appointment_id):
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
        appointment.delete()
        return True
    except Appointment.DoesNotExist:
        return False
    
def update_task(task_id, name=None, expected_time=None, date=None, importancy_level=None):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return None
    if name:
        task.name=name
    if date:
        task.date=date
    if expected_time:
        task.expected_time=expected_time
    if importancy_level: 
        task.importancy_level=importancy_level

    task.save()
    return task

def update_appointment(appointment_id, name=None, start_time=None, end_time=None, date=None, repetition=None):
    try:
        appointment = Appointment.objects.get(pk = appointment_id)
    except Appointment.DoesNotExist:
        return None
    if name:
        appointment.name=name
    if date:
        appointment.date=date
    if start_time:
        appointment.start_time=start_time
    if end_time: 
        appointment.end_time=end_time
    if repetition:
        appointment.repetition = repetition
    if date:
        appointment.date = date
        
    appointment.save()
    return appointment
        
def get_task(task_id):
    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return None
    return task.name, task.expected_time , task.date, task.importancy_level

def get_appointment(appointment_id):
    try:
        appointment = Appointment.objects.get(pk = appointment_id)
    except Appointment.DoesNotExist:
        return None
    return appointment.name, appointment.start_time,appointment.end_time,appointment.date,appointment.repetition