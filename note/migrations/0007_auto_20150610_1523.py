# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0006_auto_20150610_1441'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notegroup',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='notegroup',
            name='group',
        ),
    ]
