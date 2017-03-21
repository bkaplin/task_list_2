from tasks.models import Task, Subtask
from tasks.forms import TaskModelForm, SubtaskModelForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
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
    try:
        task = Task.objects.get(id=pk)
    except:
        context['tasks'] = Task.objects.all()
        return render(request, 'index.html', context)
    else:
        task.delete()
        mes = u'Task has been deleted.'
        messages.success(request, mes)
        context['tasks'] = Task.objects.all()
        return render(request, 'index.html', context)

def detail(request, pk):
    context = {}
    task = Task.objects.get(id=pk)
    context['detail_pk'] = int(pk)
    context['tasks'] = Task.objects.all()
    context['subtasks'] = task.subtask_set.all()
    return render(request, 'index.html', context)


# def create_subtask(request, pk):
#     context = {}
#     context['detail_pk'] = int(pk)
#     task = Task.objects.get(id=pk)
#     if request.method == "POST":
#         form = SubtaskModelForm(request.POST)
#         form.task = task
#         if form.is_valid():
#             subtask = form.save()
#             mes = u'Subtask has been successfully added.'
#             messages.success(request, mes)
#             context['tasks'] = Task.objects.all()
#             context['subtasks'] = task.subtask_set.all()
#             return render(request, 'index.html', context)
#     else:
#         form = SubtaskModelForm()
#         context['form'] = SubtaskModelForm()
#     context['new_subtask'] = int(pk)
#     context['tasks'] = Task.objects.all()
#     context['subtasks'] = task.subtask_set.all()
#     print context
#     print pk
#     return render(request, 'index.html', context)

class SubtaskCreateView(CreateView):
    model = Subtask
    template_name = "index.html"
    print "add  "
    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        task = Task.objects.get(id=pk)
        context = super(SubtaskCreateView, self).get_context_data(**kwargs)
        context['detail_pk'] = int(pk)
        context['new_subtask'] = int(pk)
        context['tasks'] = Task.objects.all()
        context['subtasks'] = task.subtask_set.all()
        print context
        return context
    # context = get_context_data(model)
    def get_success_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.object.task.id})
    def get_initial(self):
        return {'task': self.kwargs['pk']}
    def form_valid(self, form):
        message = super(SubtaskCreateView, self).form_valid(form)
        mes = "Task has been successfully added."
        messages.success(self.request, mes)
        return message


def update_subtask(request, pk):
    context = {}
    subtask = Subtask.objects.get(id=pk)
    task = Task.objects.get(id=subtask.task.pk)
    context['detail_pk'] = int(task.pk)
    if request.method == "POST":
        form = SubtaskModelForm(request.POST, instance=subtask)
        if form.is_valid():
            subtask = form.save()
            mes = u'The changes have been saved.'
            messages.success(request, mes)
            # context['form'] = TaskModelForm(instance=task)
            context['tasks'] = Task.objects.all()
            context['subtasks'] = task.subtask_set.all()
            return render(request, 'index.html', context)
    else:
        form = SubtaskModelForm(instance=subtask)
        context['form'] = SubtaskModelForm(instance=subtask)
    context['subtask_update_pk'] = int(pk)
    context['subtasks'] = task.subtask_set.all()
    context['tasks'] = Task.objects.all()
    print context
    print task.pk
    return render(request, 'index.html', context)

def remove_subtask(request, pk):
    context = {}
    context['detail_pk'] = int(pk)
    # print context
    try:
        subtask = Subtask.objects.get(id=pk)
        task = Task.objects.get(id=subtask.task.pk)
        context['detail_pk'] = int(task.pk)
    except:
        context['tasks'] = Task.objects.all()
        return render(request, 'index.html', context)
    else:
        subtask.delete()
        mes = u'Subask has been deleted.'
        messages.success(request, mes)
        context['tasks'] = Task.objects.all()
        context['subtasks'] = task.subtask_set.all()
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
