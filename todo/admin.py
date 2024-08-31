from django.contrib import admin
from .models import Task, WorkDone, FamilyMember,Parents

# Register your models here.

admin.site.register(Task)
admin.site.register(WorkDone)

admin.site.register(FamilyMember)

admin.site.register(Parents)
