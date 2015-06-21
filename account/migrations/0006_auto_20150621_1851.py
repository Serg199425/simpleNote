# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import awesome_avatar.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20150621_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=awesome_avatar.fields.AvatarField(default=b'image.jpg', upload_to=b'avatars'),
        ),
    ]
