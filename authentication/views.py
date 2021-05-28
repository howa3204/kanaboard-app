from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from billing.models import StripeCustomer

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard')
            else:
                messages.error(request, 'Incorrect username or password', extra_tags='incorrect')

    context = {}
    return render(request, 'authentication/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('authentication:login')

def subscription_check(user):
    customer = StripeCustomer.objects.get(owner=user)

    return customer.status == 'active' or customer.status == 'trialing'

@login_required(login_url='authentication:login')
def sorry(request):
    return render(request, 'authentication/sorry.html')
