from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from functools import wraps

import json

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

    # handle event
    if event.type == 'subscription.created':
        handle_create_subscription(event)
    if event.type == 'subscription.updated':
        handle_update_subscription(event)

    return HttpResponse(status=200)




def handle_create_subscription(event):
    pass

def handle_update_subscription(event):
    pass
