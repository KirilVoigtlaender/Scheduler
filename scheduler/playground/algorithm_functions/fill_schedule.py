from ..models import Appointment


def fill_schedule(start_of_week, end_of_week, filled_schedule, repetition_appointments):
    
    #Fill the array with the appointments and scheduled appointments from Uni
    appointments_of_the_week = Appointment.objects.filter(date__gte = start_of_week, date__lte = end_of_week)

    for appointment in appointments_of_the_week:
        apt_date = appointment.date
        apt_weekday = apt_date.weekday()
        start_time_obj = appointment.start_time
        end_time_obj = appointment.end_time

        # Calculate the number of minutes since midnight for start and end times
        start_minutes_since_midnight = start_time_obj.hour * 60 + start_time_obj.minute
        end_minutes_since_midnight = end_time_obj.hour * 60 + end_time_obj.minute

        # Calculate the corresponding values from 0 to 95 for start and end times
        start_time_value = start_minutes_since_midnight // 15
        end_time_value = end_minutes_since_midnight // 15

        for timeslot in range(start_time_value, end_time_value):
            filled_schedule[apt_weekday][timeslot] = True
        #Now we know the free time of the week to work

    for appointment in repetition_appointments:
        if appointment.date <= end_of_week:
            apt_date = appointment.date
            apt_weekday = apt_date.weekday()
            start_time_obj = appointment.start_time
            end_time_obj = appointment.end_time

            # Calculate the number of minutes since midnight for start and end times
            start_minutes_since_midnight = start_time_obj.hour * 60 + start_time_obj.minute
            end_minutes_since_midnight = end_time_obj.hour * 60 + end_time_obj.minute

            # Calculate the corresponding values from 0 to 95 for start and end times
            start_time_value = start_minutes_since_midnight // 15
            end_time_value = end_minutes_since_midnight // 15

            for timeslot in range(start_time_value, end_time_value):
                filled_schedule[apt_weekday][timeslot] = True
            #Now we know the free time of the week to work

    return filled_schedule