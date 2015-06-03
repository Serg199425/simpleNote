# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default=b'path/to/my/default/image.jpg', upload_to=b''),
        ),
    ]
