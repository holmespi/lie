# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categories'
        db.create_table(u'content_categories', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'content', ['Categories'])

        # Adding model 'Post'
        db.create_table(u'content_post', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('date', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'content', ['Post'])

        # Adding model 'Product'
        db.create_table(u'content_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thumb', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'content', ['Product'])

        # Adding M2M table for field category on 'Product'
        m2m_table_name = db.shorten_name(u'content_product_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('product', models.ForeignKey(orm[u'content.product'], null=False)),
            ('categories', models.ForeignKey(orm[u'content.categories'], null=False))
        ))
        db.create_unique(m2m_table_name, ['product_id', 'categories_id'])

        # Adding model 'Stockist'
        db.create_table(u'content_stockist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'content', ['Stockist'])

        # Adding model 'Collection'
        db.create_table(u'content_collection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('link', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'content', ['Collection'])

        # Adding M2M table for field products on 'Collection'
        m2m_table_name = db.shorten_name(u'content_collection_products')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('collection', models.ForeignKey(orm[u'content.collection'], null=False)),
            ('product', models.ForeignKey(orm[u'content.product'], null=False))
        ))
        db.create_unique(m2m_table_name, ['collection_id', 'product_id'])


    def backwards(self, orm):
        # Deleting model 'Categories'
        db.delete_table(u'content_categories')

        # Deleting model 'Post'
        db.delete_table(u'content_post')

        # Deleting model 'Product'
        db.delete_table(u'content_product')

        # Removing M2M table for field category on 'Product'
        db.delete_table(db.shorten_name(u'content_product_category'))

        # Deleting model 'Stockist'
        db.delete_table(u'content_stockist')

        # Deleting model 'Collection'
        db.delete_table(u'content_collection')

        # Removing M2M table for field products on 'Collection'
        db.delete_table(db.shorten_name(u'content_collection_products'))


    models = {
        u'content.categories': {
            'Meta': {'ordering': "('category',)", 'object_name': 'Categories'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'content.collection': {
            'Meta': {'object_name': 'Collection'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'products': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['content.Product']", 'symmetrical': 'False'})
        },
        u'content.post': {
            'Meta': {'object_name': 'Post'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'content.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['content.Categories']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'stock': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thumb': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'content.stockist': {
            'Meta': {'object_name': 'Stockist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['content']