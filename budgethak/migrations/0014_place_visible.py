# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgethak', '0013_auto_20160719_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
