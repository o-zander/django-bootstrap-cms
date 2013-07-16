from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models
from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

from .utils import truncate_text


class Row(CMSPlugin):
    identifier = models.CharField(_('ID'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Row')
        verbose_name_plural = _('Rows')

    def __unicode__(self):
        return '#%s' % (self.identifier or self.id)


class Column(CMSPlugin):
    SPANS = ((x, x) for x in range(1, 13))
    OFFSETS = ((x, x) for x in range(13))

    span = models.IntegerField(_('Span'), choices=SPANS, default=3)
    offset = models.IntegerField(_('Offset'), choices=OFFSETS, default=0, blank=True)
    identifier = models.CharField(_('ID'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Column')
        verbose_name_plural = _('Columns')

    def __unicode__(self):
        return '#%s (%s-%i %s-%i)' % (self.identifier or self.id, _('Span'), self.span, _('Offset'), self.offset)


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

    content = models.TextField(_('Text'))
    lead = models.BooleanField(_('Lead'), blank=True, default=False)
    align = models.CharField(_('Alignment'), max_length=11, choices=ALIGNMENTS, blank=True)
    emphasis = models.CharField(_('Emphasis'), max_length=12, choices=EMPHASES, blank=True)
    identifier = models.CharField(_('ID'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Paragraph')
        verbose_name_plural = _('Paragraphs')

    def __unicode__(self):
        return '#%s [%s]' % (self.identifier or self.id, truncate_text(self.content, limit=40))

    def get_class_attributes(self):
        return ['lead' if self.lead else '', self.align, self.emphasis]

    def has_class(self):
        return any(self.get_class_attributes())

    def get_class(self):
        return u' '.join([cls for cls in self.get_class_attributes() if cls])


class Headline(CMSPlugin):
    RANKS = ((x, 'H%i' % x) for x in range(1, 7))

    rank = models.PositiveSmallIntegerField(_('Rank'), choices=RANKS, default=2)
    content = models.TextField(_('Text'))
    identifier = models.CharField(_('ID'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Headline')
        verbose_name_plural = _('Headlines')

    def __unicode__(self):
        return '#%s (%s) [%s]' % (
            self.identifier or self.id,
            self.get_rank_display(),
            truncate_text(self.content, limit=40)
        )


class BlockQuote(CMSPlugin):
    ALIGNMENTS = (
        (0, _('Left')),
        (1, _('Right')),
    )

    align = models.PositiveSmallIntegerField(_('Alignment'), choices=ALIGNMENTS, blank=True, default=0)
    source = models.TextField(_('Source'), blank=True)
    identifier = models.CharField(_('ID'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Blockquote')
        verbose_name_plural = _('Blockquote')

    def __unicode__(self):
        if self.source:
            return '#%s [%s]' % (self.identifier or self.id, truncate_text(self.source, limit=40))
        return '#%s' % self.identifier or self.id

    def get_alignment_class(self):
        if self.align == 1:
            return 'pull-right'
        return ''


class Image(CMSPlugin):
    SHAPES = (
        ('rounded', _('Rounded')),
        ('circle', _('Circle')),
        ('polaroid', _('Polaroid')),
    )

    file = FilerImageField(verbose_name=_('Image'), related_name='image_plugin_images',
                           null=True, on_delete=models.SET_NULL)
    alt = models.CharField(_('Alternative text'), max_length=200, blank=True)
    shape = models.CharField(_('Shape'), max_length=8, choices=SHAPES, blank=True,
                             help_text=_("The settings 'Rounded' and 'Circle' are not supported in IE 7/8"))
    identifier = models.CharField(_('ID'), max_length=200, blank=True)

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __unicode__(self):
        return '#%s (%s) [%s]' % (
            self.identifier or self.id,
            self.get_shape_display() if self.shape else _('Normal'),
            self.file.original_filename if self.file else _('Image has been deleted!'),
        )

    def get_alternative_text(self):
        if self.alt:
            return self.alt
        if self.file:
            return self.file.default_alt_text or self.file.original_filename
        return _('Image #%(id)s has been deleted' % {'id': self.id})






