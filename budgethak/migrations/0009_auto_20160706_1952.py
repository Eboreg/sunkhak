# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('budgethak', '0008_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghours',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opening_hours', to='budgethak.Place'),
        ),
    ]
