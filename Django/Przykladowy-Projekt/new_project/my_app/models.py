from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    title = models.CharField(max_length=80)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    published_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
