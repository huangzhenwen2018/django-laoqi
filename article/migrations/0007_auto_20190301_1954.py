# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2019-03-01 11:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20190301_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='article_tag',
            field=models.ManyToManyField(blank=True, related_name='article_tag', to='article.ArticleTag'),
        ),
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 1, 11, 54, 2, 720243, tzinfo=utc)),
        ),
    ]