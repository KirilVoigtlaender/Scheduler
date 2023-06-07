from datetime import timedelta
def sort_tasks(sorted_tasks, freetime, filled_schedule, start_of_week):
    for task in range(len(sorted_tasks)):
        for day in range(7):
            if sorted_tasks[task].date == start_of_week + timedelta(days=day):
                tasktime = float(sorted_tasks[task].expected_time)*4
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
                        for i in range(task_slots): # If there are enough slots free after eachother schedule the task
                            if filled_schedule[max_free_day][slot+i] != False:
                                all_available = False
                                break

                        if all_available:
                            start_slot = slot
                            break
        
                    # Update the filled_schedule array to mark the time slots as occupied
                    for slot in range(start_slot, start_slot + task_slots):
                        filled_schedule[max_free_day][slot] = sorted_tasks[task].name

                    # Update the freetime array to subtract the occupied time slots
                    freetime[max_free_day] = freetime[max_free_day] - (task_slots * 15)
                    tasktime = tasktime - task_slots
                    if tasktime <= 0:
                        break
    return filled_schedule