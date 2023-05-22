from models import Task
from datetime import date

def algorithm():
    today = date.today()
    #tasks = Task.objects.filter(date__gt=today).order_by('date')  #ordered list after dates
    expected = Task.objects.filter(date_gt=today).order_by('expected_time') #ordered list after expected time
    #list = []  #here we want to insert the sorted stuff ater the calculations then 
    date_importancy = Task.objects.filter(date__gt=today).order_by('-importancy_level', 'date')
    
    

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

    
    for i in range(len(date_importancy)):   
        if(date_importancy[i].expected_time < date_importancy[i+1].expected_time):
                    switch = date_importancy[i]
                    date_importancy[i] = date_importancy[i+1]
                    date_importancy[i+1] = switch




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
#                   if no we can leave it as it is 
