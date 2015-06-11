from django.db import models
from account.fields import AutoOneToOneField
from django.contrib.auth.models import User
from IPython import embed

class Account(models.Model):
	user = AutoOneToOneField(User, related_name='account', verbose_name=('User'), primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	avatar = models.ImageField(default='image.jpg')

	def full_name(self):
		return self.first_name + " " + self.last_name

	def image(self):
		if self.avatar.url == '/media/False':
			return "/media/image.jpg"
		else:
			return self.avatar.url

class Friendship(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	creator = models.ForeignKey(User, related_name="friendship_creator_set")
	friend = models.ForeignKey(User, related_name="friend_set")
	confirmed = models.BooleanField(blank=True)
	class Meta:
		unique_together = ('creator', 'friend',)
        auto_created = True
