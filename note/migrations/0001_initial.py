# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import redactor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('short_text', redactor.fields.RedactorField(verbose_name='Text')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NoteGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.ForeignKey(to='groups.Group')),
                ('note', models.ForeignKey(to='note.Note')),
            ],
        ),
        migrations.CreateModel(
            name='NoteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.ForeignKey(to='note.Note')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='groups',
            field=models.ManyToManyField(to='groups.Group', through='note.NoteGroup'),
        ),
        migrations.AddField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(related_name='note_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='note',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='note.NoteUser'),
        ),
        migrations.AlterUniqueTogether(
            name='noteuser',
            unique_together=set([('user', 'note')]),
        ),
        migrations.AlterUniqueTogether(
            name='notegroup',
            unique_together=set([('group', 'note')]),
        ),
    ]
