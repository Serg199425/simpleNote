# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20150608_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.ForeignKey(to='note.Note')),
            ],
        ),
    ]
