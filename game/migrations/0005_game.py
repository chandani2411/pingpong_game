# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 10:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20170716_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.IntegerField()),
                ('winner', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]