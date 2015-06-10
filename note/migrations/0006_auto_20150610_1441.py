# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0005_auto_20150610_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notegroup',
            name='group',
            field=select2.fields.ForeignKey(to='groups.Group'),
        ),
    ]
