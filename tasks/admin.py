from django.contrib import admin
from tasks.models import Task, Subtask

class SubtaskInline(admin.TabularInline):
	model = Subtask
	extra = 0

class TaskAdmin(admin.ModelAdmin):
	list_display = ['description']
	fields = ['description']
	inlines = [SubtaskInline]


admin.site.register(Task, TaskAdmin)
admin.site.register(Subtask)