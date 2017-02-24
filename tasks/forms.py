# -*- coding: utf-8 -*-
from django import forms
from tasks.models import Task, Subtask

class symbolWidget(forms.Textarea):
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('attrs', {}).update({'rows': 3, 'cols': 40})
		super(symbolWidget, self).__init__(*args, **kwargs)

class TaskModelForm(forms.ModelForm):
	class Meta:
		model = Task
	fields = '__all__'#['description']
	description = forms.CharField(widget=symbolWidget, max_length=70, label=u'Описание')

class SubtaskModelForm(forms.ModelForm):
	class Meta:
		model = Subtask
	fields = '__all__'#['description']
	description = forms.CharField(widget=symbolWidget, max_length=70, label=u'Описание')