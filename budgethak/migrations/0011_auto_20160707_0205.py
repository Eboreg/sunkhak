# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgethak', '0010_auto_20160706_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
    ]
