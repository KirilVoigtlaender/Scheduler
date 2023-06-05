from .models import Task, Appointment
from datetime import date, timedelta, datetime, time
from .algorithm_functions.initialize_schedule import initialize_schedule
from .algorithm_functions.fill_schedule import fill_schedule
from .algorithm_functions.calculate_daily_freetime import calculate_daily_freetime

def algorithm():
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    
    #Specify here when your preferred working hours are, now specified as not between 0 and 7, and 23 and 24
    unpreferred_timeslots = [[0, 7*4-1], [23*4, 24*4-1]]
    
    #add appointments from repetition, make it an argument of algorithm()
    repetition_appointments = []
    
    #Initialize the schedule with the timeslots corrisponding to the unpreferred timeslots filled
    initialized_schedule = initialize_schedule(unpreferred_timeslots)


    #Fill the schedule with the appointments and scheduled appointments from Uni
    filled_schedule = fill_schedule(start_of_week, end_of_week, initialized_schedule, repetition_appointments)

    #Sort all tasks with a deadline after or on today, by importancy and date
    sorted_tasks = sorted(Task.objects.filter(date__gte = today), key=lambda x: (-x.importancy_level, x.date))

    # Calculate how much freetime you have on each day of the week
    freetime = calculate_daily_freetime(filled_schedule)
    
    for task in range(len(sorted_tasks)):
        for day in range(7):
            if sorted_tasks[task].date == start_of_week + timedelta(days=day):
                #print(sorted_tasks[task].date.strftime)
                tasktime = float(sorted_tasks[task].expected_time)*4
                #print("The task time is:", tasktime)
                while True:
                    max_free_day, timefree = 0, 0
                    for days in range(day):
                        if freetime[days] > timefree:
                            max_free_day, timefree = days, freetime[days]
                    if tasktime >= 2:
                        task_slots = 2
                    else:
                        task_slots = 1
                    start_slot = None
                    for slot in range(96 - task_slots + 1):  # Iterate over all possible starting slots
                        all_available = True
                        for i in range(task_slots):
                            if filled_schedule[max_free_day][slot+i] != False:
                                all_available = False
                            #    print("Kareem says we stopped the loop.")
                                break

                        if all_available:
                            start_slot = slot
                            break

                        # if all(not filled_schedule[max_free_day][slot+i] for i in range(task_slots)):
                        #     start_slot = slot
                        #     break
                            
                    # Update the filled_schedule array to mark the time slots as occupied
                    for slot in range(start_slot, start_slot + task_slots):
                        filled_schedule[max_free_day][slot] = sorted_tasks[task].name
                        print("here", slot, max_free_day, tasktime)

                    # Update the freetime array to subtract the occupied time slots
                    freetime[max_free_day] = freetime[max_free_day] - (task_slots * 15)
                    tasktime = tasktime - task_slots
                    print(tasktime)
                    if tasktime <= 0:
                        break

  
    to_schedule = []
    for day in range(len(filled_schedule)):
        slot = 0
        while slot < len(filled_schedule[day]):
            if not(filled_schedule[day][slot] == True) and not(filled_schedule[day][slot] == False):
                #starting_point = datetime.time(slot//4, slot%4*15, 0) 
                starting_time = datetime(2000,1,1) + timedelta(minutes=slot * 15)
                #+ timedelta(minutes=slot * 15)).strftime("%H:%M")
                ending_time = datetime(2000,1,1) + timedelta(minutes=slot * 15 + 15)
                for endslot in range(slot+1,len(filled_schedule[day])):
                    if filled_schedule[day][slot] == filled_schedule[day][endslot]:
                        slot = slot+1
                        #ending_point_str = 
                        #ending_point = time(0, 0, 0) + timedelta(minutes=slot * 15 + 15)
                        #ending_point = timedelta(minutes=endslot*15+15)
                        #ending_point_time = datetime.strptime(ending_point_str, "%H:%M").time()
                        ending_time = datetime(2000,1,1) + timedelta(minutes=slot * 15 + 15)
                # starting_datetime = datetime.combine(start_of_week + timedelta(days=day), starting_time)
                # ending_datetime = datetime.combine(start_of_week + timedelta(days=day), ending_time)
                appointment = Appointment()
                appointment.name = filled_schedule[day][slot]  # Replace with the appropriate value
                appointment.start_time = starting_time.time()
                appointment.end_time = ending_time.time()
                appointment.date = start_of_week + timedelta(days=day)  # Replace with the appropriate value
                appointment.repetition = 1  # Replace with the appropriate repetition value
                to_schedule.append(appointment) 
            slot = slot+1
    for task in to_schedule:
        print(task.name)
        print(task.start_time)  
        print(task.end_time) 
        print(task.date) 
        print(task.repetition)      
    return to_schedule
    #print(to_schedule)
    #for day in range(7):
    #    for element in range(len(filled_schedule[day])):
    #        print(filled_schedule[day][element])      
# 0= 00:00 , 1= 0:15,2= 0:30, 3= 0:45, 4 = 1
                    
# how many extra assingments we give on a day so that the average 
#  per day is equal almost
# and then need to find a way to put it imnto the schedule
        #compute a good time / maybe one or many depends on the expected time
        #while computed time is already taken, compute a new time
