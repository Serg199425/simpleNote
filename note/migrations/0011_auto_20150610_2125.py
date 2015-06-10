# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0010_auto_20150610_2038'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='noteuser',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='noteuser',
            name='note',
        ),
        migrations.RemoveField(
            model_name='noteuser',
            name='user',
        ),
        migrations.AddField(
            model_name='note',
            name='users',
            field=models.ManyToManyField(related_name='note_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(related_name='note_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='NoteUser',
        ),
    ]
