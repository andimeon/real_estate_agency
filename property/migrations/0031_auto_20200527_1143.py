# Generated by Django 2.2.4 on 2020-05-27 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0030_auto_20200521_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='claim',
            old_name='user',
            new_name='customer',
        ),
    ]
