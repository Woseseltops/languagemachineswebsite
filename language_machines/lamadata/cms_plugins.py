from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from language_machines.lamadata.models import Person, Project, Software

class TeamListPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "teamlist_plugin.html"

    def render(self, context, instance, placeholder):
        context['persons'] = Person.objects.order_by('firstname')
        return context


class SoftwareListPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "softwarelist_plugin.html"

    def render(self, context, instance, placeholder):
        context['software'] = Software.objects.order_by('name')
        return context

class ProjectListPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "projectlist_plugin.html"

    def render(self, context, instance, placeholder):
        context['projects'] = Project.objects.order_by('name')
        return context

plugin_pool.register_plugin(TeamListPlugin)
plugin_pool.register_plugin(SoftwareListPlugin)
plugin_pool.register_plugin(ProjectListPlugin)
