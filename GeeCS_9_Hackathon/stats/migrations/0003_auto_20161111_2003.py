# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20161111_2000'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Question',
            new_name='Subject',
        ),
    ]
