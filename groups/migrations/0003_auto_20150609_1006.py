# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='confirmed',
        ),
        migrations.AddField(
            model_name='groupuser',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
