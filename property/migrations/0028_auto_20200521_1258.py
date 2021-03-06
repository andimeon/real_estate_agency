# Generated by Django 2.2.4 on 2020-05-21 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0027_flat_liked_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='flats_owner',
            new_name='flat_owner',
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='flats_owner', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
