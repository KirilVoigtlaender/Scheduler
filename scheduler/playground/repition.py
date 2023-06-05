from .models import  Appointment
from datetime import date, timedelta, datetime, time
from dateutil.relativedelta import relativedelta

def reptition():
    all_appointment = Appointment.objects.all()

    to_appointment= []
    for appointment in all_appointment:
        if appointment.repetition != 1:
                if appointment.repetition == 2:
                    for i in range (1,30):
                        new_appointment = Appointment()
                        new_appointment.name = appointment.name  # Replace with the appropriate value
                        new_appointment.start_time = appointment.start_time
                        new_appointment.end_time = appointment.end_time
                        new_appointment.date = appointment.date + timedelta(days=i)  # Replace with the appropriate value
                        new_appointment.repetition = 1  # Replace with the appropriate repetition value
                        to_appointment.append(new_appointment)
                        #Append it somewhere
                if appointment.repetition == 3:
                    for i in range (1,52):
                        new_appointment = Appointment()
                        new_appointment.name = appointment.name  # Replace with the appropriate value
                        new_appointment.start_time = appointment.start_time
                        new_appointment.end_time = appointment.end_time
                        new_appointment.date = appointment.date + timedelta(weeks=i)  # Replace with the appropriate value
                        new_appointment.repetition = 1  # Replace with the appropriate repetition value
                        to_appointment.append(new_appointment)
                        #Append it somewhere
                if appointment.repetition == 4:
                    for i in range (1,12):
                        new_appointment = Appointment()
                        new_appointment.name = appointment.name  # Replace with the appropriate value
                        new_appointment.start_time = appointment.start_time
                        new_appointment.end_time = appointment.end_time
                        new_appointment.date = appointment.date + relativedelta(month=+i+1)  # Replace with the appropriate value
                        new_appointment.repetition = 1  # Replace with the appropriate repetition value
                        to_appointment.append(new_appointment)
                        #Append it somewhere
    return to_appointment       

   