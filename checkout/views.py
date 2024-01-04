from django.shortcuts import render, redirect, reverse

from django.contrib import messages

from .forms import OrderForm
# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OUy0ZApuZfiR6v74rbqDkch0SwQUIA0AucxS5EfmkNKfphPzckcPN3Oaf7S31gSa9ZUk0oKUigSwlzfMdMJAFch00sv4PdbPr',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)