from django.db import models
from django.db.models import Model

class Event(models.Model):
    REPETITION_VALUES = (
        ('Never', 'Never'),
        ('Every Day', 'Every Day'),
        ('Every Week', 'Every Week'),
        ('Every Month', 'Every Month'),
        ('Every Year', 'Every Year')
    )
    TYPE_VALUE = (
        ('Appointment', 'Appointment'),
        ('Task', 'Task'),
        ('Schedule','Schedule')
    )
    name = models.CharField(max_length=50)
    event_type = models.CharField(choices= TYPE_VALUE,max_length=20,default= 'Task')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    repetition = models.CharField(choices= REPETITION_VALUES, max_length=20, default='Never') #In the add task,add appointment it 
                                                                                                #is named as importancy level

