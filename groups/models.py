from django.db import models

class Group(models.Model):
	creator = models.ForeignKey('account.User', related_name='group_creator')
	name = models.CharField(max_length=250)
	date = models.DateTimeField(auto_now_add=True, blank=True)
	users = models.ManyToManyField('account.User', through='GroupUser')
	def __str__(self):
		return self.name

class GroupUser(models.Model):
	group = models.ForeignKey(Group)
	user = models.ForeignKey('account.User')
	is_creator = models.BooleanField(default=False)
	confirmed = models.BooleanField(default=False)
	class Meta:
		unique_together = ('group', 'user',)

