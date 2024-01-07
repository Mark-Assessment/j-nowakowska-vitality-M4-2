from django.shortcuts import render

# Create your views here.
def profile(request):
    """ Iser's profile view """

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)