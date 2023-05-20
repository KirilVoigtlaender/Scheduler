from django import forms



#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
#from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from .models import Task,Appointment

class AddTaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields= ['name', 'expected_time', 'date', 'importancy_level']

class AddAppointmentForm(forms.ModelForm):
    class Meta:
        model= Appointment
        fields = ['name', 'start_time','end_time', 'date','repetition']
        

