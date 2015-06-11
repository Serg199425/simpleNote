# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('account', models.ForeignKey(to='account.Account')),
                ('group', models.ForeignKey(to='groups.Group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='accounts',
            field=models.ManyToManyField(to='account.Account', through='groups.GroupAccount'),
        ),
        migrations.AddField(
            model_name='group',
            name='creator',
            field=models.ForeignKey(related_name='group_creator', to='account.Account'),
        ),
        migrations.AlterUniqueTogether(
            name='groupaccount',
            unique_together=set([('group', 'account')]),
        ),
    ]
