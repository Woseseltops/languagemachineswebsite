from django.contrib import admin
from language_machines.lamadata.models import Person, Project, Software

admin.site.register(Person)
admin.site.register(Project)
admin.site.register(Software)
