# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20170720_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='defencive_array',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]