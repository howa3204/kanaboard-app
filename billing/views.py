import hashlib
import hmac
import json
import datetime

import sendgrid
import stripe

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from registration.models import CustomUser

from .models import StripeCustomer

# Create your views here.

# Display Billflow billing page.
@login_required(login_url='authentication:login')
def billing(request):
    billflow_secret = settings.BILLFLOW_SECRET
    billing_page_id = settings.BILLING_PAGE_ID
    user_email = request.user.email
    email_hash = hmac.new(
    billflow_secret.encode('ascii'), # SECRET KEY (KEEP SAFE!)
    request.user.email.encode('ascii'), # REPLACE WITH USER'S EMAIL ADDRESS
    digestmod=hashlib.sha256 # HASH FUNCTION
    ).hexdigest() # PASS THIS TO FRONT-END

    context = {
        'user_email':user_email,
        'email_hash':email_hash,
        'billing_page_id':billing_page_id,
    }
    return render(request, 'billing/billing.html', context)

# Connect to Stripe Webhooks.
@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
          json.loads(payload), endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)

    # Handle the event.
    if event['type'] == 'customer.created':
        customer = event['data']['object']

        # Retrieve email and customer_id from customer.created webhook.
        email = customer.get('email')
        customer_id = customer.get('id')

        # Save CustomUser object to database.
        user = CustomUser.objects.get(email=email)
        StripeCustomer.objects.create(
            owner = user,
            customer_id = customer_id,
            subscription_id = 'none',
            status = 'trialing')

    if event['type'] == 'customer.subscription.created':
        subscription = event['data']['object']

        # Fetch all the required data from session.
        customer_id = subscription.get('customer')
        subscription_id = subscription.get('id')
        status = subscription.get('status')
        customer = stripe.Customer.retrieve(customer_id)

        # Save StripeCustomer model in database.
        user = CustomUser.objects.get(email=customer.email)
        customer = StripeCustomer.objects.get(customer_id=customer_id)
        customer.subscription_id = subscription_id
        customer.status = status
        customer.save()

    if event['type'] == 'customer.subscription.updated':
        subscription = event['data']['object']

        # Fetch all the required data from session.
        customer_id = subscription.get('customer')
        status = subscription.get('status')

        # Update StripeCustomer Model for subscription update.
        customer = StripeCustomer.objects.get(customer_id=customer_id)
        customer.status = status
        customer.save()

    if event['type'] == 'customer.subscription.deleted':
        subscription = event['data']['object']

        # Fetch all the required data from session.
        customer_id = subscription.get('customer')
        status = subscription.get('status')

        # Update StripeCustomer Model for subscription cancellation.
        customer = StripeCustomer.objects.get(customer_id=customer_id)
        customer.status = status
        customer.save()
        user = CustomUser.objects.get(username=customer.owner)

        # Email change confirmation message.
        subject = 'Subscription Cancellation'
        body = 'Hi ' + user.first_name + ',\n' + '\n' + "We're confirming that your Kanaboard subscription has been cancelled." + '\n' + '\n' + "If you didn't make this change, please contact as soon as possible by replying to this email." + '\n' + '\n' + 'Best,' + '\n' + 'The Kanaboard Team'

        email = EmailMessage(
            subject,
            body,
            'Kanaboard <accounts@kanaboard.com>',
            [user.email],
        )
        email.send(fail_silently=False)

    if event['type'] == 'invoice.payment_failed':
        invoice = event['data']['object']

        # Fetch all the required data from session.
        customer_id = invoice.get('customer')
        customer = StripeCustomer.objects.get(customer_id=customer_id)
        subscription = stripe.Subscription.retrieve(customer.subscription_id)
        customer = stripe.Customer.retrieve(customer_id)
        invoice_id = invoice.get('id')

        # Perform checks.
        now = datetime.datetime.fromtimestamp(int(invoice.get('created')))
        trial_start = datetime.datetime.fromtimestamp(int(customer.created))
        days_since = (now - trial_start).days

        # Cancel subscription if 14 days since subscription start and no billing details added.
        if days_since < 15 :
            stripe.Subscription.delete(subscription)
            stripe.Invoice.void_invoice(invoice_id)
        else:
            pass

    if event['type'] == 'customer.subscription.trial_will_end':
        subscription = event['data']['object']

        # Fetch all the required data from session.
        customer_id = subscription.get('customer')
        customer = StripeCustomer.objects.get(customer_id=customer_id)
        user = CustomUser.objects.get(username=customer.owner)

        # Notify user that free trial will end in 3 days.
        subject = 'Free Trial Ending'
        body = 'Hi ' + user.first_name + ',\n' + '\n' + "Thanks for using Kanaboard. In 3 days your free trial will end. If you would like to continue using Kanaboard, please log into your account and update your payment information by following the steps below:" + '\n' + '\n' + '1. Log into your account and click on the My Account button in the top right hand corner.' + '\n' + '2. Click on Billing.' + '\n' + "3. Click on 'Change Plan' in the middle of the billing page." + '\n' + "4. Select the monthly or yearly subscription then click 'Select Plan'." + '\n' + "5. Enter your payment information and confirm." + '\n' + '\n' + "If you have any questions please reach out to us." + '\n' + '\n' + 'Best,' + '\n' + 'The Kanaboard Team'

        email = EmailMessage(
            subject,
            body,
            'Kanaboard <accounts@kanaboard.com>',
            [user.email],
        )
        email.send(fail_silently=False)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)
