# Generated by Django 2.2.4 on 2020-05-20 14:06

from django.db import migrations


def switch_owner_phone_model(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        flat_owner_phonenumber = flat.owners_phonenumber
        flat_owner_pure_phonenumber = flat.owner_phone_pure
        Owner.objects.get_or_create(owner_number=flat_owner_phonenumber)
        Owner.objects.get_or_create(owner_number_norm=flat_owner_pure_phonenumber)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0015_auto_20200520_1655'),
    ]
    
    operations = [
        migrations.RunPython(switch_owner_phone_model)
    ]