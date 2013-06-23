from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import Row


class RowPlugin(CMSPluginBase):
    model = Row
    name = _('Row')
    render_template = 'components/row.html'

plugin_pool.register_plugin(RowPlugin)