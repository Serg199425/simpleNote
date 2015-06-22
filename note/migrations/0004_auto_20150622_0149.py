# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20150620_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='short_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
