# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20150611_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='short_text',
            field=redactor.fields.RedactorField(verbose_name='Text'),
        ),
    ]
