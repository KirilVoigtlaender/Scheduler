from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path("", views.index, name='base'),
    path("home", views.home, name='home'),
    path('add_task', views.add_task),
    path('add_appointment', views.add_appointment),
]