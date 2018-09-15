from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, render_to_response
from .forms import LoginRegistrationForm
from django.urls import reverse


# Create your views here.
def login_register(request):
    if request.method == 'POST':
        form = LoginRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect(reverse('login_register_success'))

    else:
        form = LoginRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


def login_register_success(request):
    return render_to_response('registration/login_register_success.html')
