# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-02-18 07:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20190218_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 7, 20, 4, 259710, tzinfo=utc)),
        ),
    ]
