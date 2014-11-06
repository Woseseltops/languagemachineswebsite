from django.conf.urls import url
#from django.conf import settings

from language_machines.lamadata.views import projectindex, projectview

urlpatterns = [
    url(r'^$', projectindex, name='projects'),
    url(r'^(?P<project_id>[A-Za-z0-9_\']+)/$', projectview, name='project'),
]
