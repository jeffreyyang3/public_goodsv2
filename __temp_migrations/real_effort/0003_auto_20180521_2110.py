# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-22 04:10
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('real_effort', '0002_auto_20180521_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='ratio',
            field=otree.db.models.IntegerField(null=True),
        ),
    ]
