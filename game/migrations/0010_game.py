# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 18:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_auto_20170720_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid', models.IntegerField()),
                ('round_winners', models.CharField(max_length=8)),
            ],
        ),
    ]
