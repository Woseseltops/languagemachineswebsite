from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from language_machines.lamadata.models import Person, Project, Software

class PersonPluginIndex(CMSPluginBase):
    model = CMSPlugin
    render_template = "person_plugin_index.html"

    def render(self, context, instance, placeholder):
        context['persons'] = Person.objects.order_by('firstname')
        return context


class SoftwarePluginIndex(CMSPluginBase):
    model = CMSPlugin
    render_template = "software_plugin_index.html"

    def render(self, context, instance, placeholder):
        context['software'] = Software.objects.order_by('name')
        return context

class ProjectPluginIndex(CMSPluginBase):
    model = CMSPlugin
    render_template = "project_plugin_index.html"

    def render(self, context, instance, placeholder):
        context['projects'] = Project.objects.order_by('name')
        return context

plugin_pool.register_plugin(PersonPluginIndex)
plugin_pool.register_plugin(SoftwarePluginIndex)
plugin_pool.register_plugin(ProjectPluginIndex)
