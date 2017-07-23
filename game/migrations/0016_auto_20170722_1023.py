# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_auto_20170721_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refree',
            name='winners',
        ),
        migrations.AddField(
            model_name='player',
            name='refree',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player', to='game.Refree'),
        ),
    ]