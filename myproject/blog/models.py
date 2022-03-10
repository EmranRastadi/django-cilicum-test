from django.db import models
from django.utils import timezone


# Create your models here.

class Articles(models.Model):
    STATUS_CHOICES = (
        ('d', 'draft'),
        ('p', 'published')
    )
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")  # thumbnail must uploaded to images folder
    publish = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title
