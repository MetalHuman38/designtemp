# uidir/models.py
from django.db import models


class Consultation(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    requirements = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}"


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname}"
