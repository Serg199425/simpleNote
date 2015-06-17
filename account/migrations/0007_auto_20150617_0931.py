# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_account_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendship',
            name='creator',
            field=models.ForeignKey(related_name='creator', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='from_friend',
            field=models.ForeignKey(related_name='from_friend', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='friendship',
            name='to_friend',
            field=models.ForeignKey(related_name='to_friend', to='account.Account'),
        ),
    ]
