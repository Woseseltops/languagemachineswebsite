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

apphook_pool.register(PersonAppHook)
apphook_pool.register(ProjectAppHook)
apphook_pool.register(PersonAppHook)
