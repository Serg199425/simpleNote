# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0015_auto_20150610_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='users',
            field=models.ManyToManyField(related_name='noteusers', to=settings.AUTH_USER_MODEL),
        ),
    ]