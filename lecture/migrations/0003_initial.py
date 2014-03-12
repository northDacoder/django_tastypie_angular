# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Class'
        db.create_table(u'lecture_class', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=75)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'lecture', ['Class'])

        # Adding model 'Student'
        db.create_table(u'lecture_student', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('klass', self.gf('django.db.models.fields.related.ForeignKey')(related_name='students', to=orm['lecture.Class'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'lecture', ['Student'])

        # Adding model 'StudentProject'
        db.create_table(u'lecture_studentproject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(related_name='projects', to=orm['lecture.Student'])),
        ))
        db.send_create_signal(u'lecture', ['StudentProject'])


    def backwards(self, orm):
        # Deleting model 'Class'
        db.delete_table(u'lecture_class')

        # Deleting model 'Student'
        db.delete_table(u'lecture_student')

        # Deleting model 'StudentProject'
        db.delete_table(u'lecture_studentproject')


    models = {
        u'lecture.class': {
            'Meta': {'object_name': 'Class'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        },
        u'lecture.student': {
            'Meta': {'object_name': 'Student'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'klass': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'students'", 'to': u"orm['lecture.Class']"}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'lecture.studentproject': {
            'Meta': {'object_name': 'StudentProject'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': u"orm['lecture.Student']"})
        }
    }

    complete_apps = ['lecture']