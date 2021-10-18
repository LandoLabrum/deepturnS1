from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Lead(models.Model):
    src = models.CharField(max_length=30, null=True, blank=True)
    fname = models.CharField(max_length=30, null=True, blank=True)
    lname = models.CharField(max_length=30, null=True, blank=True)
    tel = models.CharField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=40, primary_key=True, unique=True)
    def __str__(self):
        return f'{self.email}'

