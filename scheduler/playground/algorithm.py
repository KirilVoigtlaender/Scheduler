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


    sorted_tasks = sorted(Task.objects.filter(date__gt = today), key=lambda x: (-x.importancy_level,x.date))
    
    tasks_nb = len(sorted_tasks)
    total_time = sum(task.expected_time for task in sorted_tasks)
    avg_time_per_task = total_time/tasks_nb
    
        #compute a good time / maybe one or many depends on the expected time
        #while computed time is already taken, compute a new time
        #



    
    #for i in range(len(expected)):
        #if(expected[i].importancy_level < expected[i+1].importancy_level):
       #             switch = expected[i]
      #              expected[i] = expected[i+1]
     #               expected[i+1] = switch
        

    #for i in range(len(expected)):
   #     if(expected[i].date < expected[i+1].date):
  #                  switch = expected[i]
 #                   expected[i] = expected[i+1]
#                    expected[i+1] = switch

    
    #for i in range(len(date_importancy)):   
     #   if(date_importancy[i].expected_time < date_importancy[i+1].expected_time):
      #              switch = date_importancy[i]
       #             date_importancy[i] = date_importancy[i+1]
        #            date_importancy[i+1] = switch




        #OOP -> for sunday high
        #LOGic -> for Friday high
        #calculus ->for friday high
        #aI-> for tmr low

        
    #we look at the tasks ->and then we check if currenct object has a lower importancy then the next object
    #if yes, maybe switch if no leave it as it is 


#1.Step: Create a list, which contains all Task
#2.Step: Order this list, after the date, which is the closest to today -> nearest at top
#3.Step: Create some sort of integer values for (high,-middle,-low)importance and for the expected time
#(maybe another list sorted after the excpected times)
#4.Step: Make some actual calculations and cry



#we need a secound sorting I think, which we use when we try to insert the assignment in the schedule,
#which checks wherter the  day of inserting is behind the deadline
#                   if yes move it upwards in the list and place it at a nother place
#                   if no we can leave it as it 
