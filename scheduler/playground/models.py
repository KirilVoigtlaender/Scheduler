from django.db import models
from django.db.models import Model
from datetime import date

class TimeRecord(models.Model):
    ts_date = models.DateTimeField()

    # Other fields

    def get_week(self):
        return self.ts_date.isocalendar()[1]
    def get_year(self):
        return self.ts_date.isocalendar()[0]


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
    #repetition = models.CharField(choices= REPETITION_VALUES, max_length=20, default='Never')
    repetition = models.PositiveSmallIntegerField(choices=(
        (1,"Never"),
        (2,"Every day"),
        (3,"Every Week"),
        (4,"Once a month")
    ))