from django.db import models

### Task Object model ###
class Task (models.Model):
    name = models.CharField(max_length=50)
    expected_time = models.DecimalField(decimal_places=2, max_digits=4)
    date = models.DateField()
    importancy_level = models.PositiveSmallIntegerField(choices=(
        (1,"Low"),
        (2,"Middle"),
        (3,"High"),
    ))

### Appointment object model ###
class Appointment(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    date = models.DateField()
    repetition = models.PositiveSmallIntegerField(choices=(
        (1,"Never"),
        (2,"Every day"),
        (3,"Every Week"),
        (4,"Once a month"),
    ))



