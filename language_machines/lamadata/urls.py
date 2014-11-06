from django.conf.urls import url
#from django.conf import settings

from language_machines.lamadata.views import personindex, projectindex, softwareindex,publicationindex, personview, projectview, softwareview, publicationview

urlpatterns = [
    url(r'^team/$', personindex, name='team'),
    url(r'^projects/$', projectindex, name='projects'),
    url(r'^software/$', softwareindex, name='software'),
    url(r'^publications/$', publicationindex, name='publications'),
    url(r'^team/(?P<person_id>[A-Za-z0-9_\']+)/$', personview, name='person'),
    url(r'^projects/(?P<project_id>[A-Za-z0-9_\']+)/$', projectview, name='project'),
    url(r'^software/(?P<sofware_id>[A-Za-z0-9_\']+)/$', softwareview, name='softwareview'),
    url(r'^publications/(?P<publication_id>[A-Za-z0-9_\']+)/$', publicationview, name='publication'),
]
