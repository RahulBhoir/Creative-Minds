from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (TemplateView, ListView,
                                  DetailView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from .models import Post
from .forms import PostCreationForm, PostUpdateForm


# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'


class HomePageView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            author = request.user
            post = Post.objects.create(title=title, text=text, author=author)
            return redirect(reverse('post_detail', kwargs={'pk': post.pk}))
    else:
        form = PostCreationForm()
    return render(request, 'blog/create_post.html', {'form': form})


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post


class PostDraftView(LoginRequiredMixin, ListView):
    template_name = 'blog/draft.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull=True).order_by('-publish_date')


@login_required
def published_post(request):
    posts = Post.objects.filter(author=request.user, publish_date__isnull=False).order_by('-publish_date')
    return render(request, 'blog/published_post.html', {'post_list': posts})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    template_name = 'blog/update_post.html'
    form_class = PostUpdateForm
    model = Post


class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Post
    success_url = '/'


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish_post()
    return redirect('home')
