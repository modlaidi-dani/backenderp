# Generated by Django 5.1.1 on 2024-10-03 13:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientinfo', '0002_initial'),
        ('inventory', '0001_initial'),
        ('tiers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonechange',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_bons_echange', to='tiers.client'),
        ),
        migrations.AddField(
            model_name='bonechange',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_bons_echange', to='clientinfo.store'),
        ),
    ]
