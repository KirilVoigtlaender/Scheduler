from django.contrib import admin

# Register your models here.
from .models import Task,Appointment

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Task,TaskAdmin)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Appointment,AppointmentAdmin)