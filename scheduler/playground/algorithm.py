from .models import Task
from datetime import date, timedelta
from .algorithm_functions.initialize_schedule import initialize_schedule
from .algorithm_functions.fill_schedule import fill_schedule
from .algorithm_functions.calculate_daily_freetime import calculate_daily_freetime
from .algorithm_functions.sort_tasks import sort_tasks
from .algorithm_functions.tasks_to_appointments import tasks_to_appointments

def algorithm(repetition_appointments):
    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    
    #Specify here when your preferred working hours are, now specified as not between 0 and 7, and 23 and 24
    unpreferred_timeslots = [[0, 7*4-1], [23*4, 24*4-1]]
    
    #Initialize the schedule with the timeslots corrisponding to the unpreferred timeslots filled
    initialized_schedule = initialize_schedule(unpreferred_timeslots)

    #Fill the schedule with the appointments and scheduled appointments from Uni
    filled_schedule = fill_schedule(start_of_week, end_of_week, initialized_schedule, repetition_appointments)

    #Sort all tasks with a deadline after or on today, by importancy and date
    sorted_tasks = sorted(Task.objects.filter(date__gte = today), key=lambda x: (-x.importancy_level, x.date))

    # Calculate how much freetime you have on each day of the week
    freetime = calculate_daily_freetime(filled_schedule)
    
    # Fill the schedule with the tasks 
    filled_schedule = sort_tasks(sorted_tasks, freetime, filled_schedule, start_of_week)
    
    # Turn the scheduled tasks into appointments which we can schedule in the views
    to_schedule = tasks_to_appointments(filled_schedule, start_of_week)
   
    return to_schedule
   
