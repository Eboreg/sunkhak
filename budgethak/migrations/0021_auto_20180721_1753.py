# Generated by Django 2.0.6 on 2018-07-21 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budgethak', '0020_auto_20180719_2240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placeuseredit',
            old_name='comment',
            new_name='user_comment',
        ),
    ]