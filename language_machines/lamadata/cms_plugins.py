from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from language_machines.lamadata.models import Person, Project, Software, SoftwarePluginIndexConfig, PersonPluginViewConfig, SoftwarePluginViewConfig, ProjectPluginViewConfig

class PersonPluginIndex(CMSPluginBase):
    name = "Person Plugin - Index"
    model = CMSPlugin
    render_template = "person_plugin_index.html"

    def render(self, context, instance, placeholder):
        context['persons'] = Person.objects.order_by('firstname')
        context['instance'] = instance
        return context

class PersonPluginView(CMSPlugin):
    name = "Person Plugin - View"
    model = PersonPluginViewConfig
    render_template = "person_plugin_view.html"

    def render(self, context, instance, placeholder):
        context['person'] = instance.person
        return context


class SoftwarePluginIndex(CMSPluginBase):
    name = "Software Plugin - Index"
    model = SoftwarePluginIndexConfig
    render_template = "software_plugin_index.html"

    def render(self, context, instance, placeholder):
        context['software'] = Software.objects.order_by('name')
        context['instance'] = instance
        return context


class ProjectPluginIndex(CMSPluginBase):
    name = "Project Plugin - Index"
    model = CMSPlugin
    render_template = "project_plugin_index.html"

    def render(self, context, instance, placeholder):
        context['projects'] = Project.objects.order_by('name')
        context['instance'] = instance
        return context


plugin_pool.register_plugin(PersonPluginIndex)
plugin_pool.register_plugin(PersonPluginView)
plugin_pool.register_plugin(SoftwarePluginIndex)
plugin_pool.register_plugin(ProjectPluginIndex)
