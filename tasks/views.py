from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render

from authentication.views import subscription_check

from .models import Task
from .forms import TaskForm

# Create your views here.

# Display all tasks in list view.
@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def tasks(request):
    tasks = Task.objects.filter(owner=request.user)

    context = {'tasks':tasks}
    return render(request, 'tasks/tasks.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def create_task(request):
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect('/tasks/')

    context = {'form':form}
    return render(request, 'tasks/add_task.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='settings_app:update_billing')
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)

    if task.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')

    context = {'form':form}
    return render(request, 'tasks/add_task.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect('/tasks/')

    context = {'task':task}
    return render(request, 'tasks/delete_task.html', context)
