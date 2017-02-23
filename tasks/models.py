from django.db import models
from django.forms import widgets

class Task(models.Model):
    description = models.CharField(max_length=70)

    def __unicode__(self):
        return self.description

class Subtask(models.Model):
    description  = models.CharField(max_length=70)
    task = models.ForeignKey(Task)

    def __unicode__(self):
        return self.description