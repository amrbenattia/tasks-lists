from asyncio import tasks
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# tasks = []

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task')
    # priority = forms.IntegerField(label='Priority', min_value=1, max_value=3)

# Create your views here.
def index(request):
    if not "tasks" in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/index.html', {"tasks": request.session["tasks"]})

def add(request):
    if request.method =="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            # tasks.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse('tasks:index'))
        else:
            return render(request, 'tasks/add_task.html', {"form": form})
    return render(request, 'tasks/add_task.html', {"form": NewTaskForm()})