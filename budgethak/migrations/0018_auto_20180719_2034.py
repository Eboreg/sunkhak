# Generated by Django 2.0.6 on 2018-07-19 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgethak', '0017_openinghours_data_migration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openinghours',
            name='end_weekday',
        ),
        migrations.RemoveField(
            model_name='openinghoursuseredit',
            name='end_weekday',
        ),
        migrations.RemoveField(
            model_name='placeuseredit',
            name='temporarily_closed_from',
        ),
        migrations.RemoveField(
            model_name='placeuseredit',
            name='temporarily_closed_until',
        ),
        migrations.AlterField(
            model_name='placeuseredit',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]