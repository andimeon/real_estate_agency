# Generated by Django 2.2.4 on 2020-05-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0024_remove_owner_flats'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
