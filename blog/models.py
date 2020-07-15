from django.db import models

# Create your models here.

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=200)

    def __str__(self):
        return self.title