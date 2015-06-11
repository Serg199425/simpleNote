# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import account.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', account.fields.AutoOneToOneField(related_name='account', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name=b'User')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('avatar', models.ImageField(default=b'image.jpg', upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('confirmed', models.BooleanField()),
                ('creator', models.ForeignKey(related_name='friendship_creator_set', to=settings.AUTH_USER_MODEL)),
                ('friend', models.ForeignKey(related_name='friend_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('creator', 'friend')]),
        ),
    ]
