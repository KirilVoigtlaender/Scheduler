from django import forms
from .models import Task,Appointment,PersonalPreference

### Task form ###
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

class AddTaskForm(forms.ModelForm):
    expected_time = IncrementalTimeField(widget=IncrementalTimeInput)

    class Meta:
        model = Task
        fields = ['name', 'expected_time', 'date', 'importancy_level']

### Appointment form ###
class AddAppointmentForm(forms.ModelForm):
    start_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'HH:MM'}),
        input_formats=['%H:%M']
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'HH:MM'}),
        input_formats=['%H:%M']
    )

    def clean_start_time(self):
        start_time = self.cleaned_data['start_time']
        # Check if minutes are a quarter value
        if start_time.minute % 15 != 0:
            raise forms.ValidationError("Minutes must be 00, 15, 30, or 45.")
        return start_time

    def clean_end_time(self):
        end_time = self.cleaned_data['end_time']
        # Check if minutes are a quarter value
        if end_time.minute % 15 != 0:
            raise forms.ValidationError("Minutes must be 00, 15, 30, or 45.")
        return end_time
    
    class Meta:
        model= Appointment
        fields = ['name', 'start_time','end_time', 'date','repetition']
        
### PersonalPreferences form ###
class AddPersonalPreferencesForm(forms.ModelForm):
    start_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'HH:MM'}),
        input_formats=['%H:%M']
    )
    end_time = forms.TimeField(
        widget=forms.TimeInput(format='%H:%M', attrs={'placeholder': 'HH:MM'}),
        input_formats=['%H:%M']
    )

    def clean_start_time(self):
        start_time = self.cleaned_data['start_time']
        # Check if minutes are a quarter value
        if start_time.minute % 15 != 0:
            raise forms.ValidationError("Minutes must be 00, 15, 30, or 45.")
        return start_time

    def clean_end_time(self):
        end_time = self.cleaned_data['end_time']
        # Check if minutes are a quarter value
        if end_time.minute % 15 != 0:
            raise forms.ValidationError("Minutes must be 00, 15, 30, or 45.")
        return end_time
    
    class Meta:
        model= PersonalPreference
        fields = ['name','start_time', 'end_time']