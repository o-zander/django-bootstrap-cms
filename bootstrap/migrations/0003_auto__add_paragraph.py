# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Paragraph'
        db.create_table(u'cmsplugin_paragraph', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('lead', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('align', self.gf('django.db.models.fields.CharField')(max_length=11, blank=True)),
            ('emphasis', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
        ))
        db.send_create_signal(u'bootstrap', ['Paragraph'])


    def backwards(self, orm):
        # Deleting model 'Paragraph'
        db.delete_table(u'cmsplugin_paragraph')


    models = {
        u'bootstrap.column': {
            'Meta': {'object_name': 'Column', 'db_table': "u'cmsplugin_column'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'offset': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'span': ('django.db.models.fields.IntegerField', [], {'default': '3'})
        },
        u'bootstrap.paragraph': {
            'Meta': {'object_name': 'Paragraph', 'db_table': "u'cmsplugin_paragraph'", '_ormbases': ['cms.CMSPlugin']},
            'align': ('django.db.models.fields.CharField', [], {'max_length': '11', 'blank': 'True'}),
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'emphasis': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'lead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'bootstrap.row': {
            'Meta': {'object_name': 'Row', 'db_table': "u'cmsplugin_row'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['bootstrap']