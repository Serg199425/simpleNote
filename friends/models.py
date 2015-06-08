from django.db import models
from django.contrib.auth.models import User

class Friendship(models.Model):
	created = models.DateTimeField(auto_now_add=True, editable=False)
	creator = models.ForeignKey(User, related_name="friendship_creator_set")
	friend = models.ForeignKey(User, related_name="friend_set")
	confirmed = models.BooleanField(blank=True)
	class Meta:
		unique_together = ('creator', 'friend',)
