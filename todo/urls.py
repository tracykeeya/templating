from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('family_members/', views.family_member, name='family_members'),
    path('add_family_members/', views.add_family_member, name='add_family_members'),
    path('task_list/', views.task_list, name='task_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('work_done/', views.workdone, name='work_done'),
    path('add_work_done/', views.add_workdone, name='add_work_done'),
    
]