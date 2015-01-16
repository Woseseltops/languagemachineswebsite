from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class PersonAppHook(CMSApp):
    name = _("Persons")
    urls = ["language_machines.lamadata.person_urls"]

class ProjectAppHook(CMSApp):
    name = _("Projects")
    urls = ["language_machines.lamadata.project_urls"]

class SoftwareAppHook(CMSApp):
    name = _("Software")
    urls = ["language_machines.lamadata.software_urls"]

class DemoAppHook(CMSApp):
    name = _("Demos")
    urls = ["language_machines.lamadata.demo_urls"]

class HomeAppHook(CMSApp):
    name = _("Home")
    urls = ["language_machines.lamadata.home_urls"]

class PublicationAppHook(CMSApp):
    name = _("Publication")
    urls = ["publications.urls"]


apphook_pool.register(PersonAppHook)
apphook_pool.register(ProjectAppHook)
apphook_pool.register(SoftwareAppHook)
apphook_pool.register(DemoAppHook)
apphook_pool.register(HomeAppHook)
apphook_pool.register(PublicationAppHook)
