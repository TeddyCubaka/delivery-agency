# Generated by Django 5.0 on 2024-01-26 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_created_at_user_failed_login_count_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Marchant',
            new_name='Merchant',
        ),
        migrations.RenameModel(
            old_name='MarchantType',
            new_name='MerchantType',
        ),
        migrations.RenameField(
            model_name='merchant',
            old_name='marchant_type',
            new_name='merchant_type',
        ),
        migrations.AlterModelTable(
            name='merchant',
            table='op_merchant',
        ),
        migrations.AlterModelTable(
            name='merchanttype',
            table='rf_merchant_type',
        ),
    ]
