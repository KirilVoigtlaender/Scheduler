def calculate_daily_freetime(schedule):
    freetime = []
    for day in range(7):
        freeminutes = 0
        for timeslot in range(96):
            if  schedule[day][timeslot] == False:
                freeminutes = freeminutes + 15
        freetime.append(freeminutes)
    return freetime