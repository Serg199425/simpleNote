# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20150608_1537'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set([('creator', 'friend')]),
        ),
    ]
