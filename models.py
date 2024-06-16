from django.db import models
import os

class Animation(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    animation_file = models.FileField(upload_to='animations/')

    def __str__(self):
        return self.title

    def file_type(self):
        name, extension = os.path.splitext(self.animation_file.name)
        return extension.lower()
