# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='creator',
            field=models.ForeignKey(related_name='friendship_creator_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='friend',
            field=models.ForeignKey(related_name='friend_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
