from .models import Task, Appointment
from datetime import date, timedelta, datetime

def algorithm():
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    #tasks = Task.objects.filter(date__gt=today).order_by('date')  #ordered list after dates
    #expected = Task.objects.filter(date_gt=today).order_by('expected_time') #ordered list after expected time
    #list = []  #here we want to insert the sorted stuff ater the calculations then 
    #date_importancy = Task.objects.filter(date__gt=today).order_by('-importancy_level', 'date')
    
    #Compute the schedule week by week

    # two dimensional array
    #first block going from 0-6 for the days monday-sunday
    #second block has 0-95 entrys for going in 15 minutes block over the while day
    #False if time is free, True otherwise. Starts with full False
    #filled_schedule = [[[False] for _ in range(96)] for _ in range(7)] #of one week, at the end of the week we set it to all false again
    filled_schedule = [[None] * 96 for _ in range(7)]
    for day in range (7):
        for slot in range (96):
            filled_schedule[day][slot] = False 
    
    #Maybe now we should define the sleeping time, lets say from 23:00 to 7:00
    for day in range(7):
        for slot, element in enumerate(filled_schedule[day]):
            if(slot <= 7*4) or (slot >= 23*4):
                filled_schedule[day][slot] = True

                #-> working till here 

    #Fill the array with the appointments and scheduled appointments from Uni
    appointments_of_the_week = Appointment.objects.filter(date__gt = start_of_week, date__lt = end_of_week)

    for appointment in appointments_of_the_week:
        apt_date = appointment.date
        apt_weekday = apt_date.weekday()
        start_time_str = appointment.start_time
        end_time_str = appointment.end_time
        
        # Convert start time string to datetime object
        start_time_obj = datetime.strptime(start_time_str, "%H:%M")

        # Convert end time string to datetime object
        end_time_obj = datetime.strptime(end_time_str, "%H:%M")

        # Calculate the number of minutes since midnight for start and end times
        start_minutes_since_midnight = start_time_obj.hour * 60 + start_time_obj.minute
        end_minutes_since_midnight = end_time_obj.hour * 60 + end_time_obj.minute

        # Calculate the corresponding values from 0 to 95 for start and end times
        start_time_value = start_minutes_since_midnight // 15
        end_time_value = end_minutes_since_midnight // 15

        for time in range(start_time_value, end_time_value):
            filled_schedule[apt_weekday][time] = True
        #Now we know the free time of the week to work


    
              
              
    

    sorted_tasks = sorted(Task.objects.filter(date__gt = today), key=lambda x: (-x.importancy_level,x.date))
    
    tasks_nb = len(sorted_tasks)
    total_time = sum(task.expected_time for task in sorted_tasks)
    avg_time_per_task = total_time/tasks_nb


    # Calculate how much freetime you have on each day of the week
    freetime = []
    for day in range(len(appointments_of_the_week)):
        freeminutes = 0
        for time in range(len(appointments_of_the_week[0])):
            if not filled_schedule[day][time]:
                freeminutes =+ 15
        freetime.append(freeminutes)

    
    for task in range(len(sorted_tasks)):
        for day in range(len(appointments_of_the_week)):
            if task.date == start_of_week + timedelta(days=day):
                tasktime = float(task.expected_time)/15
                while True:
                    max_free_day, timefree = 0, 0
                    for days in day:
                        if freetime[days] > timefree:
                            max_free_day, timefree = days, freetime[days]
                    
                    if tasktime >= 2:
                        task_slots = 2
                    else:
                        task_slots = 1
                    start_slot = None
                    for slot in range(96 - task_slots + 1):  # Iterate over all possible starting slots
                        if all(not filled_schedule[max_free_day][slot+i] for i in range(task_slots)):
                            start_slot = slot
                            break
                            
                    # Update the filled_schedule array to mark the time slots as occupied
                    for slot in range(start_slot, start_slot + task_slots):
                        filled_schedule[max_free_day][slot] = task.name

                    # Update the freetime array to subtract the occupied time slots
                    freetime[max_free_day] =- task_slots * 15

                    tasktime =- task_slots
                    if tasktime <= 0:
                        break
  
    to_schedule = []
    for day in range(len(filled_schedule)):
        for slot in range(len(filled_schedule[day])):
            if not(filled_schedule[day][slot] == True) and not(filled_schedule[day][slot] == False):
                starting_point = timedelta(minutes=slot*15)
                ending_point = timedelta(minutes=slot*15+15)
                for endslot in range(slot+1,len(filled_schedule[day])):
                    if filled_schedule[day][slot] == filled_schedule[day][endslot]:
                        slot = slot+1
                        ending_point = timedelta(minutes=endslot*15+15)
                appointment = Appointment()
                appointment.name = filled_schedule[day][slot]  # Replace with the appropriate value
                appointment.start_time = starting_point  # Replace with the appropriate value
                appointment.end_time = ending_point  # Replace with the appropriate value
                appointment.date = day  # Replace with the appropriate value
                appointment.repetition = 1  # Replace with the appropriate repetition value
                to_schedule.append(appointment) 

    for day in range(7):
        for element in range(len(filled_schedule[day])):
            print(filled_schedule[day][element])      
# 0= 00:00 , 1= 0:15,2= 0:30, 3= 0:45, 4 = 1
                    
# how many extra assingments we give on a day so that the average 
#  per day is equal almost
# and then need to find a way to put it imnto the schedule
        
        
    
        #compute a good time / maybe one or many depends on the expected time
        #while computed time is already taken, compute a new time
        
 