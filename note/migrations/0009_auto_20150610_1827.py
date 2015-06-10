# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_group_notes'),
        ('note', '0008_auto_20150610_1527'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NoteShare',
            new_name='NoteUser',
        ),
        migrations.AddField(
            model_name='note',
            name='groups',
            field=models.ManyToManyField(to='groups.Group', through='note.NoteGroup'),
        ),
    ]
