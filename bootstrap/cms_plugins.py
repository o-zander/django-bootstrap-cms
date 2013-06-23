from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import Row, Column, Paragraph


class RowPlugin(CMSPluginBase):
    model = Row
    name = _('Row')
    render_template = 'components/row.html'
    allow_children = True
    child_classes = ['ColumnPlugin']


plugin_pool.register_plugin(RowPlugin)


class ColumnPlugin(CMSPluginBase):
    model = Column
    name = _('Column')
    render_template = 'components/column.html'
    allow_children = True
    child_classes = ['RowPlugin', 'ParagraphPlugin']

plugin_pool.register_plugin(ColumnPlugin)


class ParagraphPlugin(CMSPluginBase):
    model = Paragraph
    name = _('Paragraph')
    render_template = 'components/paragraph.html'

plugin_pool.register_plugin(ParagraphPlugin)