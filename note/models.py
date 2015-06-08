from django.db import models
from redactor.fields import RedactorField
from django.contrib.auth.models import User

class Note(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=250, verbose_name=u'Title')
	short_text = RedactorField(
		verbose_name=u'Text',
		redactor_options={'lang': 'en', 'focus': 'true'},
		upload_to='media/',
		allow_file_upload=True,
		allow_image_upload=True
	)
	date = models.DateTimeField(auto_now_add=True, blank=True)

class NoteShare(models.Model):
	note = models.ForeignKey(Note)
	user = models.ForeignKey(User)
	class Meta:
		unique_together = ('note', 'user',)
		
