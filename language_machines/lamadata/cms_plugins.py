from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from language_machines.lamadata.models import Person, Project, Software, SoftwareIndex, PersonView, SoftwareView, ProjectView

class PersonIndexPlugin(CMSPluginBase):
    name = "Person Index Plugin"
    model = CMSPlugin
    render_template = "person_index_plugin.html"

    def render(self, context, instance, placeholder):
        context['persons'] = Person.objects.order_by('firstname')
        context['instance'] = instance
        return context

class PersonViewPlugin(CMSPluginBase):
    name = "Person View Plugin"
    model = PersonView
    render_template = "person_view_plugin.html"

    def render(self, context, instance, placeholder):
        context['person'] = instance.person
        return context

    def copy_relations(self, oldinstance):
        self.person = oldinstance.person.all()


class SoftwareIndexPlugin(CMSPluginBase):
    name = "Software Index Plugin"
    model = SoftwareIndex
    render_template = "software_index_plugin.html"

    def render(self, context, instance, placeholder):
        context['software'] = Software.objects.order_by('name')
        context['instance'] = instance
        return context

class SoftwareViewPlugin(CMSPluginBase):
    name = "Software View Plugin"
    model = SoftwareView
    render_template = "software_view_plugin.html"

    def render(self, context, instance, placeholder):
        context['software'] = instance.person
        return context

    def copy_relations(self, oldinstance):
        self.person = oldinstance.person.all()

class ProjectIndexPlugin(CMSPluginBase):
    name = "Project Index Plugin"
    model = CMSPlugin
    render_template = "project_index_plugin.html"

    def render(self, context, instance, placeholder):
        context['projects'] = Project.objects.order_by('name')
        context['instance'] = instance
        return context

class ProjectViewPlugin(CMSPluginBase):
    name = "Project View Plugin"
    model = ProjectView
    render_template = "project_view_plugin.html"

    def render(self, context, instance, placeholder):
        context['project'] = instance.project
        return context

    def copy_relations(self, oldinstance):
        self.person = oldinstance.person.all()



plugin_pool.register_plugin(PersonIndexPlugin)
plugin_pool.register_plugin(PersonViewPlugin)
plugin_pool.register_plugin(SoftwareIndexPlugin)
plugin_pool.register_plugin(ProjectIndexPlugin)
