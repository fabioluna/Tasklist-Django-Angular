from django.conf.urls import url
from django.contrib import admin

from tasklist_app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/$', views.task_list),
    url(r'^tasks/new', views.task_create),
    url(r'^tasks/update/(?P<pk>[0-9]+)$', views.task_update),
    url(r'^tasks/delete/(?P<pk>[0-9]+)$', views.task_delete),
]
