# Generated by Django 5.0 on 2024-01-30 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_address_unique_address'),
        ('user', '0012_alter_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.address'),
        ),
    ]
