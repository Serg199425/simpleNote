from django.db import models
from django.db.models import Q
from groups.models import Group
from tagging_autocomplete_tagit.models import TagAutocompleteTagItField
from ckeditor.fields import RichTextField
from django.conf import settings
import redis
from django.core import serializers
from IPython import embed

ORDERS_FREE_LOCK_TIME = getattr(settings, 'ORDERS_FREE_LOCK_TIME', 0)
ORDERS_REDIS_HOST = getattr(settings, 'ORDERS_REDIS_HOST', 'localhost')
ORDERS_REDIS_PORT = getattr(settings, 'ORDERS_REDIS_PORT', 6379)
ORDERS_REDIS_PASSWORD = getattr(settings, 'ORDERS_REDIS_PASSWORD', None)
ORDERS_REDIS_DB = getattr(settings, 'ORDERS_REDIS_DB', 0)

service_queue = redis.StrictRedis(
    host=ORDERS_REDIS_HOST,
    port=ORDERS_REDIS_PORT,
    db=ORDERS_REDIS_DB,
    password=ORDERS_REDIS_PASSWORD
).publish

class Note(models.Model):
	owner = models.ForeignKey('account.User', related_name='note_owner')
	title = models.CharField(max_length=250, verbose_name=u'Title')
	short_text = RichTextField(config_name='awesome_ckeditor')
	date = models.DateTimeField(auto_now_add=True, blank=True)
	groups = models.ManyToManyField(Group, through='NoteGroup')
	users = models.ManyToManyField('account.User', through='NoteUser')
	favorite_users = models.ManyToManyField('account.User', through='FavoriteNote', related_name='favorite_notes')
	tags = TagAutocompleteTagItField(max_tags=False, blank=True)
	def save_users_and_groups(self, users, groups):
		self.notegroup_set.all().delete()
		self.noteuser_set.all().delete()
		for user in users:
			NoteUser(note=self, user=user).save()
		for group in groups:
			NoteGroup(note=self, group=group).save()
		service_queue('update_notes', serializers.serialize('json', [self]))
	def has_access(self, user):
		if bool(set(user.group_set.all()) & set(self.groups.all())) or user in self.users.all():
			return True
		else:
			return False

class NoteUser(models.Model):
	note = models.ForeignKey(Note)
	user = models.ForeignKey('account.User')
	class Meta:
		unique_together = ('user', 'note')

class NoteGroup(models.Model):
	note = models.ForeignKey(Note)
	group = models.ForeignKey(Group)
	class Meta:
		unique_together = ('group', 'note',)

class FavoriteNote(models.Model):
	note = models.ForeignKey(Note)
	user = models.ForeignKey('account.User')
	class Meta:
		unique_together = ('user', 'note')
	

		
