# user_auth/models.py

from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Password will be stored securely using Django's password hashing

    def __str__(self):
        return self.username
