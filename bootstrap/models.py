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