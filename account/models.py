from django.db import models
from account.fields import AutoOneToOneField
from django.contrib.auth.models import User
from IPython import embed
from itertools import chain

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
	def friends(self):
		friends_ids = list(chain(Friendship.objects.filter(creator_id=self.user_id, confirmed=True).values_list('friend'),
					Friendship.objects.filter(friend_id=self.user_id, confirmed=True).values_list('creator')))
		if friends_ids != []:
			friends_ids = zip(*friends_ids)[0]
		return User.objects.filter(id__in=friends_ids)
	def invitations(self):
		return Friendship.objects.filter(friend_id=self.user_id, confirmed=False)

	def shared_notes(self):
		groups = self.user.groups
		notes_ids = list(chain(Friendship.objects.filter(creator_id=self.user_id, confirmed=True).values_list('friend'),
					Friendship.objects.filter(friend_id=self.user_id, confirmed=True).values_list('creator')))

class Friendship(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	creator = models.ForeignKey(User, related_name="friendship_creator_set")
	friend = models.ForeignKey(User, related_name="friend_set")
	confirmed = models.BooleanField(blank=True)
	class Meta:
		unique_together = ('creator', 'friend',)
	def get(self, user_id, current_user_id):
		friendship = Friendship.objects.filter(creator_id=user_id, friend_id=current_user_id)
		friendship |= Friendship.objects.filter(creator_id=current_user_id, friend_id=user_id)
		return friendship.first()
