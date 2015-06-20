# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tagging_autocomplete_tagit.models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_note_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=tagging_autocomplete_tagit.models.TagAutocompleteTagItField(max_length=255, blank=True),
        ),
    ]
