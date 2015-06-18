# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150618_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='shared_notes_last_seen',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
