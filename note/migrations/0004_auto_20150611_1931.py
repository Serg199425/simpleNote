# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_note_favorite_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='short_text',
            field=models.CharField(max_length=2500),
        ),
    ]
