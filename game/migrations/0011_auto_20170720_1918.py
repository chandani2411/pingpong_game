# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 19:18
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='round_winners',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='player',
            name='attacking_no',
            field=models.IntegerField(blank=True, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='defencive_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]
