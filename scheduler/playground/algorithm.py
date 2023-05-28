from models import Task, Appointment
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
    filled_schedule = [[[False]*96]*7] #of one week, at the end of the week we set it to all false again

    for row in filled_schedule:
        for element in row:
            print(element)
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
            filled_schedule[time][apt_weekday] = True
        #Now we know the free time of the week to work

    #Maybe know we should define the sleeping time, lets say from 23:00 to 7:00
    for day in range(7):
        for time in range(23*60//15, 7*60//15):
            filled_schedule[time][day] = True


    sorted_tasks = sorted(Task.objects.filter(date__gt = today), key=lambda x: (-x.importancy_level,x.date))
    
    tasks_nb = len(sorted_tasks)
    total_time = sum(task.expected_time for task in sorted_tasks)
    avg_time_per_task = total_time/tasks_nb


    # Calculate how much freetime you have on each day of the week
    freetime = []
    for day in len(appointments_of_the_week):
        freeminutes = 0
        for time in len(appointments_of_the_week[0]):
            if not filled_schedule[time][day]:
                freeminutes =+ 15
        freetime.append(freeminutes)

    
    for task in len(sorted_tasks):
        for day in len(appointments_of_the_week):
            if task.date == start_of_week + timedelta(days=day):
                
    
# how many extra assingments we give on a day so that the average 
#  per day is equal almost
# and then need to find a way to put it imnto the schedule
        
    
        #compute a good time / maybe one or many depends on the expected time
        #while computed time is already taken, compute a new time
        
 