from django.db import models
from django.db.models import Model


class Task (models.Model):
    
    name = models.CharField(max_length=50)
    expected_time = models.TimeField()
    date = models.DateField()
    #importancy_level = models.CharField(choices=LEVEL_VALUES,max_length=50,default='Low')
    importancy_level = models.PositiveSmallIntegerField(choices=(
        (1,"Low"),
        (2,"Middle"),
        (3,"High"),
    ))

class Appointment(models.Model):
    
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    #repetition = models.CharField(choices= REPETITION_VALUES, max_length=20, default='Never')
    repetition = models.PositiveSmallIntegerField(choices=(
        (1,"Never"),
        (2,"Every day"),
        (3,"Every Week"),
        (4,"Once a month"),
    ))