from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.shortcuts import redirect, render

from authentication.views import subscription_check

from tasks.models import Task

from .forms import CourseForm
from .models import Course

# Create your views here.

# Display all courses.
@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def coursework(request):
    coursework = Course.objects.filter(owner=request.user)

    context = {'coursework':coursework}
    return render(request, 'coursework/coursework.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def add_course(request):
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect('/coursework/')

    context = {'form':form}
    return render(request, 'coursework/add_course.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def update_course(request, course_id):
    course = Course.objects.get(id=course_id)
    form = CourseForm(instance=course)

    if course.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('/coursework/')

    context = {'form':form}
    return render(request, 'coursework/add_course.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        course.delete()
        return redirect('/coursework/')

    context = {'course':course}
    return render(request, 'coursework/delete_course.html', context)
