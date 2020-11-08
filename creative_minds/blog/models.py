from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse_lazy


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(User, default=0, on_delete=models.SET_DEFAULT)
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    @staticmethod
    def get_absolute_url():
        return reverse_lazy('home')

    def publish_post(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
