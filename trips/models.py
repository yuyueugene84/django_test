from django.db import models

# Create your models here.
class Post(models.Model):

    def __str__(self):
        return "title: " + self.title + " content: " + self.content

    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)