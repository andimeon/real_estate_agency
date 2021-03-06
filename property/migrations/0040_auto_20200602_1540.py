# Generated by Django 2.2.4 on 2020-06-02 12:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0039_auto_20200601_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='claim_writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='claims', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='rooms_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='property.Flat', verbose_name='Номер комнаты'),
        ),
    ]
