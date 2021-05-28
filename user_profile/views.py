import stripe

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import Http404
from django.shortcuts import render, redirect
from registration.models import CustomUser, Profile

from .forms import CustomUserForm
from billing.models import StripeCustomer

# Create your views here.

@login_required(login_url='authentication:login')
def profile(request):

    context = {}
    return render(request, 'user_profile/profile.html', context)

@login_required(login_url='authentication:login')
def update_profile(request):
    profile = CustomUser.objects.get(username=request.user)
    form = CustomUserForm(instance=request.user)

    if profile.username != request.user.username:
        raise Http404

    if request.method == 'POST':
        old_email = request.user.email
        old_username = request.user.username

        form = CustomUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            new_email = form.cleaned_data.get('email')
            new_username = form.cleaned_data.get('username')

            if new_email != old_email:

                # Update Stripe customer email address.
                stripe_customer = StripeCustomer.objects.get(owner=request.user)
                stripe_customer_id = stripe_customer.stripe_customer_id

                stripe.Customer.modify(
                    stripe_customer_id,
                    email = new_email,
                )

                # Email variables.
                subject = 'Email Change'
                body = 'Hi ' + request.user.first_name + ',\n' + '\n' + "We're confirming that you updated the email associated with your account. Your new email is " + request.user.email + '.\n' + '\n' + "If you didn't make this change, please contact as soon as possible by replying to this email." + '\n' + '\n' + 'Best,' + '\n' + 'The Kanaboard Team'

                # Email change confirmation message.
                email = EmailMessage(
                    subject,
                    body,
                    'Kanaboard <accounts@kanaboard.com>',
                    [new_email],
                )
                email.send(fail_silently=False)

                email = EmailMessage(
                    subject,
                    body,
                    'Kanaboard <accounts@kanaboard.com>',
                    [old_email],
                )
                email.send(fail_silently=False)

            if new_username != old_username:

                # Email variables.
                subject = 'Username Change'
                body = 'Hi ' + request.user.first_name + ',\n' + '\n' + "We're confirming that you updated the username associated with your Kanaboard account. Your new username is " + request.user.username + '.\n' + '\n' + "If you didn't make this change, please contact us as soon as possible by replying to this email." + '\n' + '\n' + 'Best,' + '\n' + 'The Kanaboard Team'

                # Username change confirmation message.
                email = EmailMessage(
                    subject,
                    body,
                    'Kanaboard <accounts@kanaboard.com>',
                    [new_email],
                )
                email.send(fail_silently=False)

        messages.success(request, 'Profile updated!')
        return redirect('/profile/')

    context = {'form':form}
    return render(request, 'user_profile/update_profile.html', context)
