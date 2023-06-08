def initialize_schedule(unpreferred_timeslots):
    TIMES_SLOTS = 96 
    WEEK_DAYS = 7
    # two dimensional array
    #first block going from 0-6 for the days monday-sunday
    #second block has 0-95 entrys for going in 15 minutes block over the whole day
    #False if time is free, True otherwise. Starts with full False
    #filled_schedule = [[[False] for _ in range(96)] for _ in range(7)] #of one week, at the end of the week we set it to all false again
    filled_schedule = [[None] * TIMES_SLOTS for _ in range(WEEK_DAYS)]
    for day in range (WEEK_DAYS):
        for slot in range (TIMES_SLOTS):
            filled_schedule[day][slot] = False 
    
    #Maybe now we should define the sleeping time, lets say from 23:00 to 7:00
    for start_slot, end_slot in unpreferred_timeslots:
        for day in range(WEEK_DAYS):
            for slot in range(len(filled_schedule[day])):
                if start_slot <= slot <= end_slot:
                    filled_schedule[day][slot] = True
    return filled_schedule