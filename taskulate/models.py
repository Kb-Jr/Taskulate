from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from ToDo import settings
# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=350, null=False, blank=False)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'


class User(AbstractUser):
    pass