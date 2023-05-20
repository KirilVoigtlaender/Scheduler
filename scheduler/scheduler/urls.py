"""
URL configuration for scheduler project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from playground import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('playground/', include('playground.urls'))
    path('',views.index),
    path('task', views.task_list, name='task_list'),#Task
    path('task/add', views.add_task, name='add_task'),#Task
    path('task/<int:pk>/remove', views.remove_task, name='remove_task'),#Task
    path('task/<int:pk>/edit', views.edit_task, name='edit_task'),#Task
    path('appointment', views.appointment_list, name='appointment_list'),#Appointment
    path('appointment/add', views.add_appointment, name='add_appointment'),#Appointment
    path('appointment/<int:pk>/remove', views.remove_appointment, name='remove_appointment'),#Appointment
    path('appointment/<int:pk>/edit', views.edit_appointment, name='edit_appointment'),#Appointmnet
    path('website/', views.website),
]
