from .models import  Appointment
from datetime import  timedelta
from dateutil.relativedelta import relativedelta

def repitition_handler(appointment, to_appointment, timefun, rangeval):
    for i in range (1, rangeval):
        new_appointment = Appointment()
        new_appointment.name = appointment.name  
        new_appointment.start_time = appointment.start_time
        new_appointment.end_time = appointment.end_time
        new_appointment.date = appointment.date + timefun * i
        new_appointment.repetition = 1  
        to_appointment.append(new_appointment)
    return

def reptition():
    all_appointment = Appointment.objects.all()
    to_appointment= []
    for appointment in all_appointment:
        if appointment.repetition != 1:
                if appointment.repetition == 2:
                    repitition_handler(appointment, to_appointment, timedelta(days=1), 365)
                elif appointment.repetition == 3:
                    repitition_handler(appointment, to_appointment, timedelta(weeks=1), 52)
                elif appointment.repetition == 4:
                    repitition_handler(appointment, to_appointment, relativedelta(months=1), 12)
    return to_appointment       

   