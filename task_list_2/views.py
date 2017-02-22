from tasks.models import Task
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
# from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def start(request):
    return render(request, 'start.html', {'tasks':Task.objects.all()})

# def index(request):
#     return render(request, 'index.html', {'tasks':Task.objects.all()})
#
# class TaskCreateView(CreateView):
#     model = Task
#     template_name = "index.html"
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super(TaskCreateView, self).get_context_data(**kwargs)
#         context['title'] = "Task creation"
#         context['new_task'] = True
#         return context
#
#     def form_valid(self, form):
#         message = super(TaskCreateView, self).form_valid(form)
#         mes = "Task has been successfully added."
#         messages.success(self.request, mes)
#         return message
#
# class TaskUpdateView(UpdateView):
#     model = Task
#     template_name = "index.html"
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super(TaskUpdateView, self).get_context_data(**kwargs)
#         context['title'] = "Task update"
#         context['update_pk'] = self.object.pk
#         return context
#
#     # def get_success_url(self):
#     #     return reverse_lazy('tasks:edit', kwargs={'pk': self.object.pk})
#
#     def form_valid(self, form):
#         message = super(TaskUpdateView, self).form_valid(form)
#         mes = "The changes have been saved."
#         messages.success(self.request, mes)
#         return super(TaskUpdateView, self).form_valid(form)
#
# class TaskDeleteView(DeleteView):
#     model = Task
#     template_name = "index.html"
#     success_url = reverse_lazy('index')
#
#     def get_context_data(self, **kwargs):
#         context = super(TaskDeleteView, self).get_context_data(**kwargs)
#         context['title'] = "Task deletion."
#         context['remove_pk'] = self.object.pk
#         return context
#
#     def delete(self, request, *args, **kwargs):
#         ret_msg = super(TaskDeleteView, self).delete(request, *args, **kwargs)
#         mes = "Task has been deleted."
#         messages.success(self.request, mes)
#         return ret_msg
