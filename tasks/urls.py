from django.conf.urls import patterns, include, url
from django.contrib import admin
# from tasks.views import index, TaskCreateView, TaskUpdateView, TaskDeleteView
from tasks.views import index, create, remove, update
urlpatterns = patterns('',
    # Examples:
    url(r'^list$', index, name='index'),
    # url(r'^$', TaskCreateView.as_view(), name='add'),
    # url(r'^update/(?P<pk>\d+)$', TaskUpdateView.as_view(), name='update'),
    # url(r'^(?P<pk>\d+)$', TaskDeleteView.as_view(), name='remove'),

    url(r'^add$', create, name='add'),
    url(r'^update/(?P<pk>\d+)$', update, name='update'),
    url(r'^remove/(?P<pk>\d+)$', remove, name='remove'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),
)
