# Generated by Django 5.0 on 2024-01-26 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_country_acronym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='acronym',
            field=models.CharField(default=None, max_length=3),
        ),
    ]
