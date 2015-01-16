from django.conf.urls import url
#from django.conf import settings

from language_machines.lamadata.views import demoindex, softwareview

urlpatterns = [
    url(r'^$', demoindex, name='demos'),
    url(r'^(?P<software_id>[A-Za-z0-9_]+)/$', softwareview, name='demoview'),
]
