from django import forms
from tasks.models import Task

class symbolWidget(forms.Textarea):
	def __init__(self, *args, **kwargs):
		kwargs.setdefault('attrs', {}).update({'rows': 3, 'cols': 40})
		super(symbolWidget, self).__init__(*args, **kwargs)

class TaskModelForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['description']
	description = forms.CharField(widget=symbolWidget, max_length=70)


