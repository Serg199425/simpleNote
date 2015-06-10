# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20150609_1006'),
        ('note', '0007_auto_20150610_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='notegroup',
            name='group',
            field=select2.fields.ForeignKey(default=None, to='groups.Group'),
        ),
        migrations.AlterUniqueTogether(
            name='notegroup',
            unique_together=set([('group', 'note')]),
        ),
    ]
