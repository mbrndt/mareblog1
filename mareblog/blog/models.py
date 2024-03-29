from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=225)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
