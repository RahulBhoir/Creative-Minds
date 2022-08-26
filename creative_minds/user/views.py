from django.shortcuts import render, redirect
from django.contrib.auth.views import logout_then_login
from django.urls import reverse
from .forms import UserRegistrationForm


# Registration

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/registration.html', context={'form': form})


# Logout User
def logout_user(request):
    return logout_then_login(request, login_url='/login')
