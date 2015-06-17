# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150617_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='from_friend',
            field=models.ForeignKey(related_name='from_friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='to_friend',
            field=models.ForeignKey(related_name='to_friend', to=settings.AUTH_USER_MODEL),
        ),
    ]
