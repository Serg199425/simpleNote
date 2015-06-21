# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import awesome_avatar.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150618_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=awesome_avatar.fields.AvatarField(default=b'image.jpg', upload_to=b'media'),
        ),
    ]
