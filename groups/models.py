from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import redis
from django.core import serializers

ORDERS_FREE_LOCK_TIME = getattr(settings, 'ORDERS_FREE_LOCK_TIME', 0)
ORDERS_REDIS_HOST = getattr(settings, 'ORDERS_REDIS_HOST', 'localhost')
ORDERS_REDIS_PORT = getattr(settings, 'ORDERS_REDIS_PORT', 6379)
ORDERS_REDIS_PASSWORD = getattr(settings, 'ORDERS_REDIS_PASSWORD', None)
ORDERS_REDIS_DB = getattr(settings, 'ORDERS_REDIS_DB', 0)

service_queue = redis.StrictRedis(
    host=ORDERS_REDIS_HOST,
    port=ORDERS_REDIS_PORT,
    db=ORDERS_REDIS_DB,
    password=ORDERS_REDIS_PASSWORD
).publish

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


@receiver(post_save, sender=GroupUser)
def after_group_save(sender,instance, signal, created, **kwargs):
	service_queue('update_groups', serializers.serialize('json', [instance]))

