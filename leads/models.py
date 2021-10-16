from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Leads(models.Model):
    src = models.CharField(max_length=30, null=True, blank=True)
    fname = models.CharField(max_length=30, null=True, blank=True)
    lname = models.CharField(max_length=30, null=True, blank=True)
    tel = models.IntegerField(max_length=30, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True, unique=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # stripe_id = models.CharField(max_length=200, unique=True, blank=True)
    # session_id = models.CharField(max_length=300, null=True, blank=True)
    # cart = models.JSONField(null=True, blank=True, default=dict)
    # pw = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return f'{self.fname} {self.lname}'

