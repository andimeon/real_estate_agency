# Generated by Django 2.2.4 on 2020-05-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0034_auto_20200527_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='flat_owner',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
    ]
