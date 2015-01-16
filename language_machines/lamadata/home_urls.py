from django.conf.urls import url
#from django.conf import settings

from language_machines.lamadata.views import home, projectcategoryview

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^categories/(?P<projectcategory_id>[A-Za-z0-9_\']+)/$', projectcategoryview, name='projectcategory')
]
