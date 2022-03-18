from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

from .managers import FileValidator

user = get_user_model()

class Video(models.Model):
    author = models.ForeignKey(
        user,
        on_delete=models.CASCADE
    )
    file = models.FileField(validators=[FileValidator])
    #slug = models.SlugField(unique=True)
    upload = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name