from datetime import timedelta, datetime
from ..models import Appointment
def tasks_to_appointments(filled_schedule,start_of_week):
    to_schedule = []
    for day in range(len(filled_schedule)):
        slot = 0
        while slot < len(filled_schedule[day]):
            if not(filled_schedule[day][slot] == True) and not(filled_schedule[day][slot] == False):
                starting_time = datetime(2000,1,1) + timedelta(minutes=slot * 15)
                ending_time = datetime(2000,1,1) + timedelta(minutes=slot * 15 + 15)
                for endslot in range(slot+1,len(filled_schedule[day])):
                    if filled_schedule[day][slot] == filled_schedule[day][endslot]:
                        slot = slot+1
                        ending_time = datetime(2000,1,1) + timedelta(minutes=slot * 15 + 15)
                appointment = Appointment() #creaing a new appointment
                appointment.name = filled_schedule[day][slot]
                appointment.start_time = starting_time.time()
                appointment.end_time = ending_time.time()
                appointment.date = start_of_week + timedelta(days=day) 
                appointment.repetition = 1 
                to_schedule.append(appointment) 
            slot = slot+1
    return to_schedule    