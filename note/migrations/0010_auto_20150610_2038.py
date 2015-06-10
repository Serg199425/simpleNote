# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_auto_20150610_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notegroup',
            name='group',
            field=models.ForeignKey(to='groups.Group'),
        ),
    ]
