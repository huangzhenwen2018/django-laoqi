# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-03-05 09:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_auto_20190305_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d'),
        ),
    ]
