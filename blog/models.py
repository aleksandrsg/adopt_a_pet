from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title