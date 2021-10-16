from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from leads.models import Leads

class F101(models.Model):
    lead = models.OneToOneField(Leads, on_delete=models.CASCADE, unique=True, primary_key=True)
    age_range = models.CharField(max_length=30, null=True, blank=True)
    describe = models.JSONField(null=True, blank=True, default=dict)
    desire = models.CharField(max_length=350, null=True, blank=True)
    listen = models.CharField(max_length=100, null=True, blank=True)
    teachable = models.IntegerField(null=True, blank=True)
    willing = models.CharField(max_length=30, null=True, blank=True)
    change = models.CharField(max_length=350, null=True, blank=True)
    appointment = models.DateTimeField(auto_now=False, auto_now_add=False)
    submitted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.fname} {self.lname}'

