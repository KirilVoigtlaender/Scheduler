from django.db import models
from django.db.models import Model


class Task (models.Model):
    LEVEL_VALUES =(

    ('Low', 'Low'),
    ('Middle','Middle'),
    ('High','High')
    )
    name = models.CharField(max_length=50)
    expected_time = models.IntegerField()
    date = models.DateField()
    importancy_level = models.CharField(choices=LEVEL_VALUES,max_length=50,default='Low')

class Appointment(models.Model):

    
    REPETITION_VALUES = (
        ('Never', 'Never'),
        ('Every Day', 'Every Day'),
        ('Every Week', 'Every Week'),
        ('Every Month', 'Every Month'),
        ('Every Year', 'Every Year')
    )
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    repetition = models.CharField(choices= REPETITION_VALUES, max_length=20, default='Never')