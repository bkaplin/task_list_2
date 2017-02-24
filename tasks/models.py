# -*- coding: utf-8 -*-
from django.db import models
from django.forms import widgets

class Task(models.Model):
    description = models.CharField(max_length=70, verbose_name=u'Описание')

    def __unicode__(self):
        return self.description

class Subtask(models.Model):
    description = models.CharField(max_length=70, verbose_name=u'Описание')
    task = models.ForeignKey(Task, verbose_name=u'Задача')

    def __unicode__(self):
        return self.description