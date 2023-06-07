from datetime import timedelta, datetime
from ..models import Appointment
def tasks_to_appointments(filled_schedule, start_of_week): 
    to_schedule = []
    for day in range(len(filled_schedule)):
        slot = 0
        while slot < len(filled_schedule[day]):
            if type(filled_schedule[day][slot]) == str:
                starting_time = datetime(2000,1,1) + timedelta(minutes=slot * 15)
                ending_time = datetime(2000,1,1) + timedelta(minutes=slot * 15 + 15)

                for endslot in range(slot+1,len(filled_schedule[day])):
                    if filled_schedule[day][slot] == filled_schedule[day][endslot] and type(filled_schedule[day][endslot]) is str and type(filled_schedule[day][slot]) is str:
                        slot = slot+1
                        ending_time = datetime(2000,1,1) + timedelta(minutes=slot * 15 + 15)
                    else: 
                        break
                        
                appointment = Appointment() #creating a new appointment
                appointment.name = filled_schedule[day][slot]
                appointment.start_time = starting_time.time()
                appointment.end_time = ending_time.time()
                appointment.date = start_of_week + timedelta(days=day) 
                appointment.repetition = 1 
                to_schedule.append(appointment) 
            slot = slot+1
    return to_schedule    