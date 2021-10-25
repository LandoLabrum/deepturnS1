from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from lead.models import lead_model
from django.contrib.postgres.fields import ArrayField



class one_question(models.Model):
    type_options = (
        ('Autocomplete', 'Autocomplete'),
        ('Checkbox', 'Checkbox'),
        ('Chips', 'Chips'),
        ('Picker', 'Picker'),
        ('Radio', 'Radio'),
        ('Range', 'Range'),
        ('Select', 'Select'),
        ('Switch', 'Switch'),
        ('Input', 'Input'),
        ('Switch', 'Switch'),
    )

    fid= models.CharField(max_length=100, primary_key=True)
    title= models.CharField(max_length=100, null=True, blank=True)
    next = models.CharField(max_length=100, null=True, blank=True)
    type = models.CharField(max_length=20, blank=False, default='Input',
                            choices=type_options, verbose_name="type_choices")
    choices=models.CharField(max_length=600)
    

    def __str__(self):
        return self.fid


class one(models.Model):
    lead = models.OneToOneField(lead_model, on_delete=models.CASCADE)
    age_range = models.CharField(max_length=30, null=True, blank=True)
    describe = models.JSONField(null=True, blank=True, default=dict)
    desire = models.JSONField(max_length=350, null=True, blank=True)
    listen = models.CharField(max_length=100, null=True, blank=True)
    teachable = models.IntegerField(null=True, blank=True)
    willing = models.CharField(max_length=70, null=True, blank=True)
    change = models.CharField(max_length=350, null=True, blank=True)
    meeting = models.BigIntegerField(primary_key=True, unique=True)
    meeting_str = models.CharField(max_length=30,unique=True)
    submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lead
# django-formtools
# What is your age range?	Select all that describes you	Teens; 20s; 30s; 40s; 50s; 60s+	Radio
# Select all that describes you	Which aspects of your life, do you wish to improve?	I am Unsatisfied with my life and I believe nobody can help me;I am unsatisfied with my life and I need guidance, community, and encouragement;I am partly satisfied with my life and want to join a community of like-minded people;I am completely satisfied with my life and believe there are no improvements to be made	Checkbox
# Which aspects of your life, do you wish to improve?	Who do you listen to?	health;wealth;love;happiness	Checkbox

# Who do you listen to?	How teachable are you?	People who have what I want;People who don’t have what I want;Nobody, I know it all.;Everybody	Radio
# How teachable are you?	How willing are you to change to get what you want?	0;10	Range
# How willing are you to change to get what you want?	When will you be ready to change?	I am very willing, I will do whatever it takes;I am open to change, but not ready to go all in;I am open to change but it depends what it is;I am not sure at this time	Radio
# When will you be ready to change?		Now;Later	Radio