from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class LamaDataApphook(CMSApp):
    name = _("Lamadata")
    urls = ["language_machines.lamadata.urls"]

apphook_pool.register(LamaDataApphook)
