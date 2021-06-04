import stripe

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from registration.models import CustomUser

from billing.models import StripeCustomer

# Create your views here.

@login_required(login_url='authentication:login')
def account(request):
    return render(request, 'account_settings/account.html')

@login_required(login_url='authentication:login')
def settings(request):
    return render(request, 'account_settings/settings.html')

class MyPasswordChangeView(PasswordChangeView):
    template_name ='account_settings/password_change.html'
    success_url = reverse_lazy('account_settings:password_change_done')

class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account_settings/password_change_done.html'

@login_required(login_url='authentication:login')
def delete_account(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Delete Stripe customer (also cancels subscription).
            customer = StripeCustomer.objects.get(owner=request.user)
            customer_id = customer.customer_id
            stripe.Customer.delete(customer_id)

            # Delete user account.
            user = CustomUser.objects.get(username=username)
            email = user.email
            user.delete()

            # Email variables.
            subject = 'Account Deletion'
            body = 'Hi ' + request.user.first_name + ',\n' + '\n' + "We're confirming that your Kanaboard account with username " + request.user.username + ' and email ' + request.user.email + ' has been deleted. Thanks for using Kanaboard!' + '\n' + '\n' + 'Best,' + '\n' + 'The Kanaboard Team'

            # Email Account Deletion message.
            email = EmailMessage(
                subject,
                body,
                'Kanaboard <accounts@kanaboard.com>',
                [email],
            )
            email.send(fail_silently=False)

            messages.success(request, 'Your account has been deleted.')
            return redirect('authentication:login')
        else:
            messages.error(request, 'Incorrect username or password')

    return render(request, 'account_settings/delete_account.html')
