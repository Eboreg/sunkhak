# Generated by Django 2.0.6 on 2018-07-22 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgethak', '0021_auto_20180721_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeuseredit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='place_images'),
        ),
    ]
