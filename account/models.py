from django.db import models
from account.fields import AutoOneToOneField
from django.contrib.auth.models import User

class Account(models.Model):
	user = AutoOneToOneField(User, related_name='account', verbose_name=('User'), primary_key=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def full_name(self):
		return self.first_name + " " + self.last_name
