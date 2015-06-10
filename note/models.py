from django.db import models
from redactor.fields import RedactorField
from django.contrib.auth.models import User
from django.db.models import Q
from groups.models import Group
import select2.fields
from IPython import embed

class Note(models.Model):
	owner = models.ForeignKey(User, related_name='note_owner')
	title = models.CharField(max_length=250, verbose_name=u'Title')
	short_text = RedactorField(
		verbose_name=u'Text',
		redactor_options={'lang': 'en', 'focus': 'true'},
		upload_to='media/',
		allow_file_upload=True,
		allow_image_upload=True
	)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	groups = models.ManyToManyField(Group, through='NoteGroup')
	users = models.ManyToManyField(User, through='NoteUser')
	def save_users_and_groups(self, users, groups):
		self.notegroup_set.all().delete()
		self.notegroup_set.all().delete()
		for user in users:
			NoteUser(note=self, user=user).save()
		for group in groups:
			NoteGroup(note=self, group=group).save()

class NoteUser(models.Model):
	note = models.ForeignKey(Note)
	user = models.ForeignKey(User)
	class Meta:
		unique_together = ('user', 'note')
		db_table = 'note_note_users'
		auto_created = True

class NoteGroup(models.Model):
	note = models.ForeignKey(Note)
	group = models.ForeignKey(Group)
	class Meta:
		unique_together = ('group', 'note',)
        auto_created = True
		
