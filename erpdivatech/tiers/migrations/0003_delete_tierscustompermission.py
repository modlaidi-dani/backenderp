# Generated by Django 4.2.5 on 2024-11-20 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiers', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TiersCustomPermission',
        ),
    ]
