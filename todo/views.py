from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task

# Create your views here.
def addTask(request):
    # Logic for adding a task goes here
    task = request.POST['task']  # Example: Print the task to the console
    Task.objects.create(task=task)  # Save the task to the database
    return redirect('home')  # Redirect to the home page after adding the task


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()  # Save the updated task to the database
    return redirect('home') # Redirect to the home page after marking the task as done


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()  # Save the updated task to the database
    return redirect('home')  # Redirect to the home page after marking the task as done

def edit_task(request, pk):
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        get_task.task = new_task  # Update the task with the new value
        get_task.save()  # Save the updated task to the database
        return redirect('home')  # Redirect to the home page after editing the task
    else:
        context = {
            'get_task': get_task, 
        }
        return render(request, 'edit_task.html', context)  # Render the edit task template with the task context

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()  # Delete the task from the database
    return redirect('home')  # Redirect to the home page after deleting the task