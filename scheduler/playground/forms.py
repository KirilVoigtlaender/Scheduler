from django import forms



#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
#from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

from .models import Task,Appointment

class IncrementalTimeField(forms.FloatField):
    def to_python(self, value):
        value = super().to_python(value)
        if value % 0.25 != 0:
            raise forms.ValidationError('Expected time must be in increments of 0.25.')
        return value
#Allow incrementations of 0.25 only (Quarter by quarter)
class IncrementalTimeInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'step': '0.25'})
        super().__init__(*args, **kwargs)

class AddTaskForm(forms.ModelForm):
    expected_time = IncrementalTimeField(widget=IncrementalTimeInput)

    class Meta:
        model = Task
        fields = ['name', 'expected_time', 'date', 'importancy_level']

class AddAppointmentForm(forms.ModelForm):
    class Meta:
        model= Appointment
        fields = ['name', 'start_time','end_time', 'date','repetition']
        

