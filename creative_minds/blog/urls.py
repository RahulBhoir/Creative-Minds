from django.urls import path
from blog import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('create/', views.PostCreationView.as_view(), name='create_post'),
    path('draft/', views.PostDraftView.as_view(), name='draft'),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete')
]
