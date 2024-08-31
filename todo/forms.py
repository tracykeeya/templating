from django import forms
from .models import Task, FamilyMember, WorkDone


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = '__all__'


class WorkDoneForm(forms.ModelForm):
    class Meta:
        model = WorkDone
        fields = '__all__'