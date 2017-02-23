from django.conf.urls import patterns, include, url
from django.contrib import admin
# from tasks.views import index, TaskCreateView, TaskUpdateView, TaskDeleteView
from tasks.views import index, create, remove, update, update_subtask, remove_subtask, detail, SubtaskCreateView
urlpatterns = patterns('',
    # Examples: create_subtask
    url(r'^list$', index, name='index'),
    # url(r'^$', TaskCreateView.as_view(), name='add'),
    # url(r'^update/(?P<pk>\d+)$', TaskUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)$', TaskDeleteView.as_view(), name='remove'),

    url(r'^add$', create, name='add'),
    url(r'^update/(?P<pk>\d+)$', update, name='update'),
    url(r'^remove/(?P<pk>\d+)$', remove, name='remove'),
    # url(r'^(?P<pk>\d+)/add_subtask$', create_subtask, name='add_subtask'),
    url(r'^(?P<pk>\d+)/add_subtask$', SubtaskCreateView.as_view(), name='add_subtask'),
    url(r'^(?P<pk>\d+)$', detail, name='detail'),
    url(r'^update_subtask/(?P<pk>\d+)$', update_subtask, name='update_subtask'),
    url(r'^remove_subtask/(?P<pk>\d+)$', remove_subtask, name='remove_subtask'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
