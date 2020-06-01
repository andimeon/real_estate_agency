# Generated by Django 2.2.4 on 2020-06-01 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0037_auto_20200601_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='claim',
            name='website_visitor',
        ),
        migrations.AddField(
            model_name='claim',
            name='claim_writer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='claim_writers', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался'),
        ),
    ]
