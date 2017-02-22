from django.conf.urls import patterns, include, url
from django.contrib import admin
from task_list_2.views import start #, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', start, name='start'),
    # url(r'^$', TaskCreateView.as_view(), name='add'),
    # url(r'^$', TaskUpdateView.as_view(), name='update'),
    # url(r'^$', TaskDeleteView.as_view(), name='remove'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tasks/', include('tasks.urls', namespace="tasks")),
    url(r'^admin/', include(admin.site.urls)),
)
