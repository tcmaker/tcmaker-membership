from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from membership.models import Household

from datetime import datetime
from functools import wraps

import json
import stripe

def uses_stripe(view_func):
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        return view_func(request, *args, **kwargs)
    return wrapped_view

@uses_stripe
@csrf_exempt
def receive_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
          json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        # Invalid Payload
        return HttpResponse(status=400)

    print(event.type)
    # handle event
    if event.type == 'customer.subscription.created':
        handle_create_subscription(event)
    if event.type == 'customer.subscription.updated':
        handle_update_subscription(event)
    if event.type == 'invoice.created':
        handle_invoice_created(event)

    return HttpResponse(status=200)

def handle_create_subscription(event):
    subscription = event.data.object
    household = Household.objects.get(external_customer_identifier=subscription.customer)
    household.status = subscription.status
    household.valid_through = datetime.utcfromtimestamp(subscription.current_period_end)
    household.external_subscription_identifier = subscription.id
    household.save()

def handle_update_subscription(event):
    subscription = event.data.object
    household = Household.objects.get(external_customer_identifier=subscription.customer)
    household.status = subscription.status
    household.valid_through = datetime.utcfromtimestamp(subscription.current_period_end)
    household.external_subscription_identifier = subscription.id
    household.save()

def handle_invoice_created(event):
    invoice = event.data.object
    if invoice.subscription:
        stripe.Invoice.finalize_invoice(invoice.id)
        invoice.send_invoice()
