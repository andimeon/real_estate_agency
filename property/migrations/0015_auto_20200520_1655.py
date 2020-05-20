# Generated by Django 2.2.4 on 2020-05-20 13:55

from django.db import migrations


def switch_owner_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        flat_owner = flat.owner_old
        Owner.objects.get_or_create(owner=flat_owner)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0014_auto_20200520_1639'),
    ]
    
    operations = [
        migrations.RunPython(switch_owner_model)
    ]
