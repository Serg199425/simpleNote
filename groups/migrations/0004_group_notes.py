# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0008_auto_20150610_1527'),
        ('groups', '0003_auto_20150609_1006'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='notes',
            field=models.ManyToManyField(to='note.Note', through='note.NoteGroup'),
        ),
    ]
