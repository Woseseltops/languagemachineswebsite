# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Person'
        db.create_table(u'lamadata_person', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('affiliation', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('function2', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('interests', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=60, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('birth_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('joined_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('left_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
        ))
        db.send_create_signal(u'lamadata', ['Person'])

        # Adding M2M table for field publications on 'Person'
        m2m_table_name = db.shorten_name(u'lamadata_person_publications')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('person', models.ForeignKey(orm[u'lamadata.person'], null=False)),
            ('publication', models.ForeignKey(orm['publications.publication'], null=False))
        ))
        db.create_unique(m2m_table_name, ['person_id', 'publication_id'])

        # Adding model 'Software'
        db.create_table(u'lamadata_software', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('source', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('webservice', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('demo', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('documentation', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('license', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
        ))
        db.send_create_signal(u'lamadata', ['Software'])

        # Adding M2M table for field authors on 'Software'
        m2m_table_name = db.shorten_name(u'lamadata_software_authors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('software', models.ForeignKey(orm[u'lamadata.software'], null=False)),
            ('person', models.ForeignKey(orm[u'lamadata.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['software_id', 'person_id'])

        # Adding M2M table for field publications on 'Software'
        m2m_table_name = db.shorten_name(u'lamadata_software_publications')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('software', models.ForeignKey(orm[u'lamadata.software'], null=False)),
            ('publication', models.ForeignKey(orm['publications.publication'], null=False))
        ))
        db.create_unique(m2m_table_name, ['software_id', 'publication_id'])

        # Adding model 'ProjectCategory'
        db.create_table(u'lamadata_projectcategory', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'lamadata', ['ProjectCategory'])

        # Adding model 'Project'
        db.create_table(u'lamadata_project', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lamadata.ProjectCategory'], blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('sponsors', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=60, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
        ))
        db.send_create_signal(u'lamadata', ['Project'])

        # Adding M2M table for field members on 'Project'
        m2m_table_name = db.shorten_name(u'lamadata_project_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'lamadata.project'], null=False)),
            ('person', models.ForeignKey(orm[u'lamadata.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'person_id'])

        # Adding M2M table for field software on 'Project'
        m2m_table_name = db.shorten_name(u'lamadata_project_software')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'lamadata.project'], null=False)),
            ('software', models.ForeignKey(orm[u'lamadata.software'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'software_id'])

        # Adding M2M table for field publications on 'Project'
        m2m_table_name = db.shorten_name(u'lamadata_project_publications')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('project', models.ForeignKey(orm[u'lamadata.project'], null=False)),
            ('publication', models.ForeignKey(orm['publications.publication'], null=False))
        ))
        db.create_unique(m2m_table_name, ['project_id', 'publication_id'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'lamadata_person')

        # Removing M2M table for field publications on 'Person'
        db.delete_table(db.shorten_name(u'lamadata_person_publications'))

        # Deleting model 'Software'
        db.delete_table(u'lamadata_software')

        # Removing M2M table for field authors on 'Software'
        db.delete_table(db.shorten_name(u'lamadata_software_authors'))

        # Removing M2M table for field publications on 'Software'
        db.delete_table(db.shorten_name(u'lamadata_software_publications'))

        # Deleting model 'ProjectCategory'
        db.delete_table(u'lamadata_projectcategory')

        # Deleting model 'Project'
        db.delete_table(u'lamadata_project')

        # Removing M2M table for field members on 'Project'
        db.delete_table(db.shorten_name(u'lamadata_project_members'))

        # Removing M2M table for field software on 'Project'
        db.delete_table(db.shorten_name(u'lamadata_project_software'))

        # Removing M2M table for field publications on 'Project'
        db.delete_table(db.shorten_name(u'lamadata_project_publications'))


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'lamadata.person': {
            'Meta': {'ordering': "['joined_date', 'firstname', 'lastname']", 'object_name': 'Person'},
            'affiliation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'birth_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'function2': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'interests': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'joined_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'left_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['publications.Publication']", 'symmetrical': 'False', 'blank': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '60', 'blank': 'True'})
        },
        u'lamadata.project': {
            'Meta': {'ordering': "['name']", 'object_name': 'Project'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lamadata.ProjectCategory']", 'blank': 'True'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lamadata.Person']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['publications.Publication']", 'symmetrical': 'False', 'blank': 'True'}),
            'software': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lamadata.Software']", 'symmetrical': 'False', 'blank': 'True'}),
            'sponsors': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        u'lamadata.projectcategory': {
            'Meta': {'ordering': "['name']", 'object_name': 'ProjectCategory'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'lamadata.software': {
            'Meta': {'ordering': "['name']", 'object_name': 'Software'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['lamadata.Person']", 'symmetrical': 'False'}),
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'demo': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'documentation': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'license': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publications': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['publications.Publication']", 'symmetrical': 'False', 'blank': 'True'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'webservice': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'publications.list': {
            'Meta': {'ordering': "('list',)", 'object_name': 'List'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'publications.publication': {
            'Meta': {'ordering': "['-year', '-month', '-id']", 'object_name': 'Publication'},
            'abstract': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'book_title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'citekey': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'doi': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'external': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'journal': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'lists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['publications.List']", 'symmetrical': 'False', 'blank': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pages': ('publications.fields.PagesField', [], {'max_length': '32', 'blank': 'True'}),
            'pdf': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['publications.Type']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'volume': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4'})
        },
        'publications.type': {
            'Meta': {'ordering': "('order',)", 'object_name': 'Type'},
            'bibtex_types': ('django.db.models.fields.CharField', [], {'default': "'article'", 'max_length': '256'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['lamadata']