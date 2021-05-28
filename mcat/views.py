from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.shortcuts import redirect, render

from authentication.views import subscription_check

from tasks.models import Task

from .models import MCAT
from .forms import MCATForm

# Create your views here.

# Display all MCAT scores.
@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:sorry')
def mcat(request):
    mcat = MCAT.objects.filter(owner=request.user)

    context = {'mcat':mcat}
    return render(request, 'mcat/mcat.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:sorry')
def create_MCAT(request):
    form = MCATForm()

    if request.method == 'POST':
        form = MCATForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect('/mcat/')

    context = {'form':form}
    return render(request, 'mcat/add_mcat.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:sorry')
def update_MCAT(request, mcat_id):
    mcat = MCAT.objects.get(id=mcat_id)
    form = MCATForm(instance=mcat)

    if mcat.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = MCATForm(request.POST, instance=mcat)
        if form.is_valid():
            form.save()
            return redirect('/mcat/')

    context = {'form':form}
    return render(request, 'mcat/add_mcat.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:sorry')
def delete_MCAT(request, mcat_id):
    mcat = MCAT.objects.get(id=mcat_id)

    if request.method == "POST":
        mcat.delete()
        return redirect('/mcat/')

    context = {'mcat':mcat}
    return render(request, 'mcat/delete_mcat.html', context)
