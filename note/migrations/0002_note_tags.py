# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging_autocomplete.models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=tagging_autocomplete.models.TagAutocompleteField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
