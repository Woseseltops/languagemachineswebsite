from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin
from language_machines.lamadata.models import Person, Project, ProjectCategory, Software


class PersonAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

class ProjectAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

class SoftwareAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

class ProjectCategoryAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass

admin.site.register(Person, PersonAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Software, SoftwareAdmin)
