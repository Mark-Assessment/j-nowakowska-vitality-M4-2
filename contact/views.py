from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings

from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Contact
from .forms import ContactForm

# Create your views here.


def contact(request):
    """ A view to return the contact page """

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            user_message = form.cleaned_data['message']
            contact_reason = form.cleaned_data['contact_reason']

            subject = f'Vitality - contact about {contact_reason}'
            message = render_to_string(
                'contact/email_confirmation.txt', {
                    'name' : name,
                    'message' : user_message
                }
             )
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]


            send_mail(
                subject,
                message,
                email_from,
                email_to
            )

            messages.info(request, f'Your message was sent successfuly')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, f'An error occured, please try again later')

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)
