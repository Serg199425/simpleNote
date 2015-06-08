# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150603_2150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField()),
                ('creator', models.ForeignKey(related_name='friendship_creator_set', to='account.Account')),
                ('friend', models.ForeignKey(related_name='friend_set', to='account.Account')),
            ],
        ),
    ]
