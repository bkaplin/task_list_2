from tasks.models import Task
from tasks.forms import TaskModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
# from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def index(request):
    context = {}
    context['tasks'] = Task.objects.all()
    return render(request, 'index.html', context)

def create(request):
    context = {}

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            task = form.save()
            mes = u'Task has been successfully added.'
            messages.success(request, mes)
            # context['form'] = TaskModelForm()
            context['tasks'] = Task.objects.all()
            return redirect("tasks:index")
    else:
        form = TaskModelForm()
    context['new_task'] = int(1)
    context['form'] = TaskModelForm()
    context['tasks'] = Task.objects.all()
    return render(request, 'index.html', context)

def update(request, pk):
    context = {}
    task = Task.objects.get(id=pk)
    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save()
            mes = u'The changes have been saved.'
            messages.success(request, mes)
            # context['form'] = TaskModelForm(instance=task)
            context['tasks'] = Task.objects.all()
            return redirect("tasks:index")
    else:
        form = TaskModelForm(instance=task)
        context['form'] = TaskModelForm(instance=task)
    context['update_pk'] = int(pk)
    context['tasks'] = Task.objects.all()
    return render(request, 'index.html', context)

def remove(request, pk):
    context = {}
    context['remove_pk'] = int(pk)
    print context
    task = Task.objects.get(id=pk)
    task.delete()
    mes = u'Task has been deleted.'
    messages.success(request, mes)
    context['tasks'] = Task.objects.all()
    return render(request, 'index.html', context)

# class TaskCreateView(CreateView):
#     model = Task
#     template_name = "index.html"
#     success_url = reverse_lazy('index')
#     print "add  "
#     def get_context_data(self, **kwargs):
#         context = super(TaskCreateView, self).get_context_data(**kwargs)
#         context['title'] = "Task creation"
#         context['new_task'] = True
#         print context
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
#         context['update_pk'] = int(self.object.pk)
#         context['tasks'] = Task.objects.all()
#         return context
#
#     # def get_success_url(self):
#     #     return reverse_lazy('tasks:edit', kwargs={'pk': self.object.pk})
#
#     def form_valid(self, form):
#         # message = super(TaskUpdateView, self).form_valid(form)
#         # mes = "The changes have been saved."
#         # messages.success(self.request, mes)
#         return super(TaskUpdateView, self).form_valid(form)

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
