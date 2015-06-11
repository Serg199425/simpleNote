# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='groupaccount',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='groupaccount',
            name='account',
        ),
        migrations.RemoveField(
            model_name='groupaccount',
            name='group',
        ),
        migrations.RemoveField(
            model_name='group',
            name='accounts',
        ),
        migrations.AlterField(
            model_name='group',
            name='creator',
            field=models.ForeignKey(related_name='group_creator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='GroupAccount',
        ),
        migrations.AddField(
            model_name='groupuser',
            name='group',
            field=models.ForeignKey(to='groups.Group'),
        ),
        migrations.AddField(
            model_name='groupuser',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='groups.GroupUser'),
        ),
        migrations.AlterUniqueTogether(
            name='groupuser',
            unique_together=set([('group', 'user')]),
        ),
    ]
