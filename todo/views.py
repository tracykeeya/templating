from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, FamilyMember, WorkDone
from .forms import TaskForm, FamilyMemberForm, WorkDoneForm

# Create your views here.

def home(request):
    return render(request, 'todo/home.html')

# FamilyMember Views
def family_member(request):
    member = FamilyMember.objects.all()
    return render(request, 'todo/family_members.html', {'members': member})

def add_family_member(request):
    if request.method == 'POST':
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family_members')
    else:
        form = FamilyMemberForm()
    return render(request, 'todo/add_family_member.html', {'form': form})


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/add_task.html', {'form': form})

"""def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/edit_task.html', {'form': form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
"""

def workdone(request):
    workdone = WorkDone.objects.all()
    return render(request, 'todo/workdone_list.html', {'workdone': workdone})

def add_workdone(request):
    if request.method == 'POST':
        form = WorkDoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('workdone_list')
    else:
        form = WorkDoneForm()
    return render(request, 'todo/add_workdone.html', {'form': form})
