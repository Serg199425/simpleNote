from django.db import models
from note.models import NoteUser, NoteGroup, Note
from IPython import embed
from itertools import chain
from django.contrib.auth.models import AbstractUser
from simple_email_confirmation import SimpleEmailConfirmationUserMixin
from awesome_avatar.fields import AvatarField

class User(SimpleEmailConfirmationUserMixin, AbstractUser):
    pass


class Account(models.Model):
	user = models.OneToOneField(User, related_name='account', verbose_name=('User'), primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	avatar = AvatarField(default='image.jpg', width=100, height=100, upload_to='avatars')
	friends = models.ManyToManyField('self', through='Friendship', symmetrical=False, related_name='friends_set', 
									through_fields=('from_friend', 'to_friend'),)
	shared_notes_last_seen = models.DateTimeField(blank=True, null=True)
	def __unicode__(self):
		return self.full_name()
	def full_name(self):
		return self.first_name + " " + self.last_name

	def image(self):
		if self.avatar.url == '/media/False':
			return "/media/image.jpg"
		else:
			return self.avatar.url
	def friends(self):
		return Friendship.objects.filter(to_friend_id=self.user_id, confirmed=True)
	def all_friends(self):
		return Friendship.objects.filter(to_friend_id=self.user_id)
	def invitations(self):
		return Friendship.objects.filter(to_friend_id=self.user_id, confirmed=False).exclude(creator_id=self.user_id)

	def shared_notes(self):
		groups_ids = self.user.groupuser_set.all().filter(confirmed=True).values_list('group')
		notes_ids = list(NoteUser.objects.filter(user_id=self.user_id).values_list('note', flat=True))
		notes_ids.extend(NoteGroup.objects.filter(group_id__in=groups_ids).values_list('note', flat=True))
		return Note.objects.filter(id__in=notes_ids).exclude(owner_id=self.user.id)

class Friendship(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	from_friend = models.ForeignKey(Account, related_name="from_friend")
	to_friend = models.ForeignKey(Account, related_name="to_friend")
	creator = models.ForeignKey(Account, related_name="creator")
	confirmed = models.BooleanField(blank=True, default=False)
	class Meta:
		unique_together = ('from_friend', 'to_friend',)
