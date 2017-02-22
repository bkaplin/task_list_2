from django.db import models
from django.forms import widgets

class Task(models.Model):
    description = models.CharField(max_length=70)