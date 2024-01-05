from django.shortcuts import render, redirect, reverse

from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

from bag.contexts import bag_contents

import stripe
# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY


    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OUy0ZApuZfiR6v74rbqDkch0SwQUIA0AucxS5EfmkNKfphPzckcPN3Oaf7S31gSa9ZUk0oKUigSwlzfMdMJAFch00sv4PdbPr',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)