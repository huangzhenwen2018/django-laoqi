# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-03-04 06:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_auto_20190301_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 6, 31, 13, 591803, tzinfo=utc)),
        ),
    ]