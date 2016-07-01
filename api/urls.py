from django.conf.urls import patterns, url

from api.views import TaskList
from api.views import TaskDetail

urlpatterns = patterns(
    'api.views',
    url(r'^tasks/$', TaskList.as_view(), name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)', TaskDetail.as_view(), name='task_detail'),
)
