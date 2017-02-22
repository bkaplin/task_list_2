from django.contrib import admin
from tasks.models import Task

class TaskAdmin(admin.ModelAdmin):
	list_display = ['description']
	fields = ['description']

admin.site.register(Task, TaskAdmin)
