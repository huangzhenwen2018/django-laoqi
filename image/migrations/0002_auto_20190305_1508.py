# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-03-05 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(height_field=300, upload_to='images/%Y/%m/%d', width_field=300),
        ),
    ]
