from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import Http404
from django.shortcuts import redirect, render

from authentication.views import subscription_check

from tasks.models import Task

from .forms import LetterForm
from .models import Letter

# Create your views here.

# Display all letters of reccomendation.
@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def letters(request):
    letters = Letter.objects.filter(owner=request.user)

    context = {'letters':letters}
    return render(request, 'letters/letters.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def create_letter(request):
    form = LetterForm()

    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.owner = request.user
            form.save()
            return redirect('/letters/')

    context = {'form':form}
    return render(request, 'letters/add_letter.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def update_letter(request, letter_id):
    letter = Letter.objects.get(id=letter_id)
    form = LetterForm(instance=letter)

    if letter.owner != request.user:
        raise Http404

    if request.method == 'POST':
        form = LetterForm(request.POST, instance=letter)
        if form.is_valid():
            form.save()
            return redirect('/letters/')

    context = {'form':form}
    return render(request, 'letters/add_letter.html', context)

@login_required(login_url='authentication:login')
@user_passes_test(subscription_check, login_url='authentication:update_billing')
def delete_letter(request, letter_id):
    letter = Letter.objects.get(id=letter_id)

    if request.method == "POST":
        letter.delete()
        return redirect('/letters/')

    context = {'letter':letter}
    return render(request, 'letters/delete_letter.html', context)
