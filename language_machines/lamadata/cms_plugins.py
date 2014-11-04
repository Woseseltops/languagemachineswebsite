from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

class TeamListPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "teamlist_plugin.html"

class SoftwareListPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "softwarelist_plugin.html"

class ProjectListPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "projectlist_plugin.html"

plugin_pool.register_plugin(TeamListPlugin)
plugin_pool.register_plugin(SoftwareListPlugin)
plugin_pool.register_plugin(ProjectListPlugin)
