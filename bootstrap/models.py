from django.utils.translation import ugettext_lazy as _

from django.db import models
from cms.models.pluginmodel import CMSPlugin


class Row(CMSPlugin):
    identifier = models.CharField(_('ID'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Row')
        verbose_name_plural = _('Rows')

    def __unicode__(self):
        return self.identifier or unicode(self.id)


class Column(CMSPlugin):
    span = models.IntegerField(_('Span'), choices=[(x, x) for x in range(1, 13)], default=3)
    offset = models.IntegerField(_('Offset'), choices=[(x, x) for x in range(13)], default=0, blank=True)
    identifier = models.CharField(_('ID'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Column')
        verbose_name_plural = _('Columns')

    def __unicode__(self):
        return u'%s (%s-%i %s-%i)' % (self.identifier or self.id, _('Span'), self.span, _('Offset'), self.offset)


class Paragraph(CMSPlugin):
    ALIGNMENTS = (
        ('text-left', _('Left')),
        ('text-center', _('Center')),
        ('text-right', _('Right')),
    )

    EMPHASES = (
        ('muted', _('Muted')),
        ('text-warning', _('Warning')),
        ('text-error', _('Error')),
        ('text-info', _('Info')),
        ('text-success', _('Success')),
    )

    text = models.TextField(_('Text'))
    lead = models.BooleanField(_('Lead'), blank=True, default=False)
    align = models.CharField(_('Alignment'), max_length=11, choices=ALIGNMENTS, blank=True)
    emphasis = models.CharField(_('Emphasis'), max_length=12, choices=EMPHASES, blank=True)

    class Meta:
        verbose_name = _('Paragraph')
        verbose_name_plural = _('Paragraphs')

    def __unicode__(self):
        if self.text < 30:
            return self.text
        return u'%s...' % self.text[0:28]

    def get_class_attributes(self):
        return ['lead' if self.lead else '', self.align, self.emphasis]

    def has_class(self):
        return any(self.get_class_attributes())

    def get_class(self):
        return u' '.join([cls for cls in self.get_class_attributes() if cls])
