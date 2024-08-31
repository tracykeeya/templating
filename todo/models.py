from django.db import models
from datetime import datetime
"""
family members,brief of their contacts
and captures of their work and asign them to particular tasks
ther is a need for you to manage people at home and the work
to be done respectively.this can be done by making coresponding models.
models;
familyMembers(name, contact, interests)
tasks(name, description, day of the week)
workDone(family_member, task, date_done)
"""

# Create your models here.
class Task(models.Model):
    DAYS_OF_WEEK = [('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday','wednesday'), ('thursday','thursday'), ('friday','friday'), ('saturday','saturday'), ('sunday','sunday')]
    name = models.CharField(max_length=255)
    description = models.TextField()
    day_of_the_week = models.CharField(max_length=10,choices=DAYS_OF_WEEK,default='monday')

    def __str__(self):
        return self.name 

class FamilyMember(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)
    interests = models.TextField()

    def __str__(self):
        return self.name
    

class WorkDone(models.Model):
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    date_done = models.DateField()
    
    def __str__(self):
        # task = (self.family_member.name) +'-'+ (self.task.name) +'-'+ (self.date_done)

        return f"{self.family_member.name} - {self.task.name} - {self.date_done}"


class Parents(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)