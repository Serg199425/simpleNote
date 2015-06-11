# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('note', '0002_auto_20150611_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='favorite_users',
            field=models.ManyToManyField(related_name='favorite_notes', through='note.FavoriteNote', to=settings.AUTH_USER_MODEL),
        ),
    ]
