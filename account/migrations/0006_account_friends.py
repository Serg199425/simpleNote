# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20150617_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='friends',
            field=models.ManyToManyField(related_name='friends_set', through='account.Friendship', to='account.Account'),
        ),
    ]
