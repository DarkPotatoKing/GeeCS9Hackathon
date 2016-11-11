# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='question',
            name='demand',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='prof',
            field=models.CharField(default='prof', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='sched',
            field=models.CharField(default='sched', max_length=1000),
        ),
        migrations.AddField(
            model_name='question',
            name='section',
            field=models.CharField(default='section', max_length=20),
        ),
        migrations.AddField(
            model_name='question',
            name='stats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.CharField(default='subj', max_length=50),
        ),
    ]
