from django.contrib import admin
from .models import Task,Appointment

### Administration manager (Editing objects from the database directly from the admin website)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Task,TaskAdmin)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Appointment,AppointmentAdmin)