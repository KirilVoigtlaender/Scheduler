from django import forms



#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
#from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from .models import Task,Appointment

class TableForm(forms.Form):
    task_name = forms.CharField (label = 'Add Task')

class TableForm(forms.Form):
    appointment_name = forms.CharField (label = 'Add Appointment')

class TableForm(forms.Form):
    repition_choices = forms.ChoiceField(label= 'Repition')

class TableForm(forms.Form):
    expected_time = forms.ChoiceField(label = 'Excpected time')

#Don't know how to use the ChoiceFiel though as we are going to give him options and he then has to select one

class AddTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields= ['name', 'expected_time', 'date', 'importancy_level']

class AddAppointmentForm(forms.ModelForm):
    class Meta:
        model= Appointment
        fields = ['name', 'start_time','end_time', 'date','repetition']
        

