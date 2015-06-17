# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0003_auto_20150611_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendship',
            name='from_friend',
            field=models.ForeignKey(related_name='from_friend', default=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendship',
            name='to_friend',
            field=models.ForeignKey(related_name='to_friend', default=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='creator',
            field=models.ForeignKey(related_name='creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('from_friend', 'to_friend')]),
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='friend',
        ),
    ]
