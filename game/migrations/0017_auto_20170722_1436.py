# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0016_auto_20170722_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='refree',
            name='scores',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='refree',
            name='winner',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
