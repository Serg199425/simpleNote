# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='friendship',
            name='friend',
        ),
        migrations.DeleteModel(
            name='Friendship',
        ),
    ]
