from django.contrib.auth.models import User
from django.db import models

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you want for authors (e.g., bio, profile picture, etc.)

    def __str__(self):
        return self.user.username
