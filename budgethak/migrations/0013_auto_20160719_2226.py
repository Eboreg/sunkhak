# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgethak', '0012_auto_20160719_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='closing_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='openinghours',
            name='opening_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
