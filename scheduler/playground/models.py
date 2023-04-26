from django.db import models
from django.db.models import Model

class Type(models.Model):
    type_text = models.CharField(max_length=200)
   

class Event(models.Model):
    name = models.CharField(max_length=50)
    event_type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()



