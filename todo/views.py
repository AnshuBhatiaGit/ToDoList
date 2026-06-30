from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Task

# Create your views here.
def addTask(request):
    # Logic for adding a task goes here
    task = request.POST['task']  # Example: Print the task to the console
    Task.objects.create(task=task)  # Save the task to the database
    return redirect('home')  # Redirect to the home page after adding the task
