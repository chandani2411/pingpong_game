# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20170717_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='attacking_no',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='defencive_array',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
