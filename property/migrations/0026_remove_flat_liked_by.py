# Generated by Django 2.2.4 on 2020-05-21 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0025_owner_flats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='liked_by',
        ),
    ]