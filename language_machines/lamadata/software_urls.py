from django.conf.urls import url
#from django.conf import settings

from language_machines.lamadata.views import softwareindex, softwareview

urlpatterns = [
    url(r'^$', softwareindex, name='software'),
    url(r'^(?P<software_id>[A-Za-z0-9_]+)/$', softwareview, name='softwareview'),
]
