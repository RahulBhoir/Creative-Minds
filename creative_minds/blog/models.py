from django.db import models
# from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse_lazy
# from user.models import Account
from django.contrib.auth import get_user_model
Account = get_user_model()

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.pk})

    def publish_post(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
