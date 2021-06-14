from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.shortcuts import render, redirect

from authentication.views import subscription_check

from tasks.models import Task

from .models import Activity
from .forms import ActivityForm

# Create your views here.

# Display all activities.
@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def activities(request):
    activities = Activity.objects.filter(owner=request.user)

    context = {'activities':activities}
    return render(request, 'activities/activities.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def add_activity(request):
    form = ActivityForm()

    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect('/activities/')

    context = {'form':form}
    return render(request, 'activities/add_activity.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def update_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    form = ActivityForm(instance=activity)

    if activity.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('/activities/')

    context = {'form':form}
    return render(request, 'activities/add_activity.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def delete_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)

    if request.method == "POST":
        activity.delete()
        return redirect('/activities/')

    context = {'activity':activity}
    return render(request, 'activities/delete_activity.html', context)
