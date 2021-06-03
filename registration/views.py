import stripe

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View

from .forms import CustomUserCreationForm
from .models import CustomUser, Profile
from .utils import account_activation_token

# Create your views here.

def register_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()

                # Create a Stripe customer.
                customer = stripe.Customer.create(
                    email = form.cleaned_data.get('email')
                    )

                # Subscribe new customer to monthly plan with a 14 day free trial.
                subscription = stripe.Subscription.create(
                    customer = customer,
                    items = [
                        {"plan": settings.STRIPE_PLAN},
                    ],
                    trial_period_days = 4,
                    )

                # Create Profile instance for new user.
                email = form.cleaned_data.get('email')
                user = CustomUser.objects.get(email=email)
                Profile.objects.create(
                    user = user,
                    current_university = None,
                    matriculation_year = None
                    )

                # Display 'Account Created' message for new user.
                user.is_active = False
                user.save()

                # Send account activation email.
                uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
                domain = get_current_site(request).domain
                link = reverse('registration:activate', kwargs={'uidb64':uidb64, 'token':account_activation_token.make_token(user)})
                activate_url = 'http://'+domain+link

                # Email variables.
                subject = 'Kanaboard Account Activation'
                body = 'Hi ' + user.first_name + ',\n' + '\n' + 'Thanks for signing up for Kanaboard. ' + 'Please click the link below to activate your account.\n' + '\n ' + activate_url + '\n' + '\n' + 'Best,\n' + 'The Kanaboard Team'

                # EmailMessage.
                email = EmailMessage(
                    subject,
                    body,
                    'Kanaboard <accounts@kanaboard.com>',
                    [email],
                )
                email.send(fail_silently=False)

                messages.success(request, 'Account successfully created. Please check your email for a link to activate your account.')
                return redirect('authentication:login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)

class Verification(View):
    def get(self, request, uidb64, token):
        User = get_user_model()
        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)

        if not account_activation_token.check_token(user, token):
            return redirect('authentication:login'+'User already activated')

        if user.is_active:
            return redirect('authentication:login')

        user.is_active = True
        user.save()
        messages.success(request, 'Account activated! You may now login.')
        return redirect('authentication:login')
