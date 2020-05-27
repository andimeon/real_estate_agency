# Generated by Django 2.2.4 on 2020-05-27 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0035_auto_20200527_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='rooms_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_active', to='property.Flat', verbose_name='Номер комнаты'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(blank=True, related_name='customers', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, related_name='owner_flat', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]