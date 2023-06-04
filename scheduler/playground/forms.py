from django import forms
from .models import Task,Appointment

### Utility classes for the TimeField to be only every quarter ###
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


### Task form ###
class AddTaskForm(forms.ModelForm):
    expected_time = IncrementalTimeField(widget=IncrementalTimeInput)

    class Meta:
        model = Task
        fields = ['name', 'expected_time', 'date', 'importancy_level']

### Appointment form ###
class AddAppointmentForm(forms.ModelForm):
    class Meta:
        model= Appointment
        fields = ['name', 'start_time','end_time', 'date','repetition']
        

