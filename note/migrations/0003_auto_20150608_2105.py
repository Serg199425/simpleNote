# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_noteshare'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='noteshare',
            unique_together=set([('note', 'user')]),
        ),
    ]
