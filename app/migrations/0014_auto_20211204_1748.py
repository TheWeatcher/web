# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-04 14:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20211204_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 4, 17, 48, 53, 453736), verbose_name='Опубликован'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 4, 17, 48, 53, 453736), verbose_name='Дата'),
        ),
    ]
