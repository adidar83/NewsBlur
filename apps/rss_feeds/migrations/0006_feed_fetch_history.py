# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FeedFetchHistory'
        db.create_table('rss_feeds_feedfetchhistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fetch_history', to=orm['rss_feeds.Feed'])),
            ('status_code', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('exception', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fetch_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('rss_feeds', ['FeedFetchHistory'])


    def backwards(self, orm):
        
        # Deleting model 'FeedFetchHistory'
        db.delete_table('rss_feeds_feedfetchhistory')


    models = {
        'rss_feeds.feed': {
            'Meta': {'object_name': 'Feed', 'db_table': "'feeds'"},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'creation': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'days_to_trim': ('django.db.models.fields.IntegerField', [], {'default': '90'}),
            'etag': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'feed_address': ('django.db.models.fields.URLField', [], {'unique': 'True', 'max_length': '255'}),
            'feed_link': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'feed_tagline': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'feed_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_load_time': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'default': '0', 'auto_now': 'True', 'blank': 'True'}),
            'min_to_decay': ('django.db.models.fields.IntegerField', [], {'default': '15'}),
            'next_scheduled_update': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'num_subscribers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'popular_authors': ('django.db.models.fields.CharField', [], {'max_length': '2048', 'null': 'True', 'blank': 'True'}),
            'popular_tags': ('django.db.models.fields.CharField', [], {'max_length': '1024', 'null': 'True', 'blank': 'True'}),
            'stories_per_month': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'rss_feeds.feedfetchhistory': {
            'Meta': {'object_name': 'FeedFetchHistory'},
            'exception': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fetch_history'", 'to': "orm['rss_feeds.Feed']"}),
            'fetch_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        'rss_feeds.feedpage': {
            'Meta': {'object_name': 'FeedPage'},
            'feed': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'feed_page'", 'unique': 'True', 'to': "orm['rss_feeds.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_data': ('utils.compressed_textfield.StoryField', [], {'null': 'True', 'blank': 'True'})
        },
        'rss_feeds.feedupdatehistory': {
            'Meta': {'object_name': 'FeedUpdateHistory'},
            'average_per_feed': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '1'}),
            'fetch_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number_of_feeds': ('django.db.models.fields.IntegerField', [], {}),
            'seconds_taken': ('django.db.models.fields.IntegerField', [], {})
        },
        'rss_feeds.feedxml': {
            'Meta': {'object_name': 'FeedXML'},
            'feed': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'feed_xml'", 'unique': 'True', 'to': "orm['rss_feeds.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rss_xml': ('utils.compressed_textfield.StoryField', [], {'null': 'True', 'blank': 'True'})
        },
        'rss_feeds.story': {
            'Meta': {'object_name': 'Story', 'db_table': "'stories'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story_author': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rss_feeds.StoryAuthor']"}),
            'story_content': ('utils.compressed_textfield.StoryField', [], {'null': 'True', 'blank': 'True'}),
            'story_content_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'story_date': ('django.db.models.fields.DateTimeField', [], {}),
            'story_feed': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stories'", 'to': "orm['rss_feeds.Feed']"}),
            'story_guid': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'story_guid_hash': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'story_original_content': ('utils.compressed_textfield.StoryField', [], {'null': 'True', 'blank': 'True'}),
            'story_past_trim_date': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'story_permalink': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'story_tags': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'story_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['rss_feeds.Tag']", 'symmetrical': 'False'})
        },
        'rss_feeds.storyauthor': {
            'Meta': {'object_name': 'StoryAuthor'},
            'author_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rss_feeds.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'rss_feeds.tag': {
            'Meta': {'object_name': 'Tag'},
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['rss_feeds.Feed']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['rss_feeds']
