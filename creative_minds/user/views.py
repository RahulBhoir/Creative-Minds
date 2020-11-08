from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout_then_login
from django.urls import reverse
from django.utils import timezone
from blog.models import Post
from blog.forms import PostCreationForm, UserRegistrationForm
# Create your views here.

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
