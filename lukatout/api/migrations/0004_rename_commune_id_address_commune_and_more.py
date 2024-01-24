# Generated by Django 5.0 on 2024-01-18 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_address_commune_province_ville_delete_categorie_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='commune_id',
            new_name='commune',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='created_by_user_id',
            new_name='created_by_user',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='province_id',
            new_name='province',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='ville_id',
            new_name='ville',
        ),
        migrations.RenameField(
            model_name='province',
            old_name='created_by_user_id',
            new_name='created_by_user',
        ),
        migrations.RenameField(
            model_name='ville',
            old_name='created_by_user_id',
            new_name='created_by_user',
        ),
        migrations.RenameField(
            model_name='ville',
            old_name='province_id',
            new_name='province',
        ),
    ]
