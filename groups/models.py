from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
	creator = models.ForeignKey(User)
	name = models.CharField(max_length=250, verbose_name=u'Name')
	date = models.DateTimeField(auto_now_add=True, blank=True)

class GroupUser(models.Model):
	group = models.ForeignKey(Group)
	user = models.ForeignKey(User)
	confirmed = models.BooleanField(default=False)
	class Meta:
		unique_together = ('group', 'user',)

