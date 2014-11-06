from django.conf.urls import url
#from django.conf import settings

from language_machines.lamadata.views import personindex, personview

urlpatterns = [
    url(r'^$', personindex, name='team'),
    url(r'^(?P<person_id>[A-Za-z0-9_\']+)/$', personview, name='person'),
]
