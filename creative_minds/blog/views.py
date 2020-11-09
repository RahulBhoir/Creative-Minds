from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (TemplateView, ListView, CreateView,
                                  DetailView, UpdateView, DeleteView)
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout_then_login
from django.urls import reverse
from django.utils import timezone
from blog.models import Post
from blog.forms import PostCreationForm, UserRegistrationForm


# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'


class HomePageView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


class PostCreationView(LoginRequiredMixin, CreateView):
    template_name = 'blog/create_post.html'
    model = Post
    # fields = ['author', 'title', 'text']
    form_class = PostCreationForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post


class PostDraftView(LoginRequiredMixin, ListView):
    template_name = 'blog/draft.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('-publish_date')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    template_name = 'blog/update_post.html'
    form_class = PostCreationForm
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish_post()
    return redirect('home')
