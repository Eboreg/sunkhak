# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 21:20
from __future__ import unicode_literals

import ajaximage.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_place_beer_price_until'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=ajaximage.fields.AjaxImageField(blank=True, null=True),
        ),
    ]
