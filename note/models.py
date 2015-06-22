from django.db import models
from redactor.fields import RedactorField
from django.db.models import Q
from groups.models import Group
import select2.fields
from IPython import embed
from tagging_autocomplete_tagit.models import TagAutocompleteTagItField
from ckeditor.fields import RichTextField

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
		
