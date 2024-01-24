# Generated by Django 5.0 on 2024-01-18 09:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_categorie_delete_todo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_by_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'op_address',
            },
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('created_by_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rf_commune',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('created_by_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'rf_province',
            },
        ),
        migrations.CreateModel(
            name='Ville',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=50)),
                ('created_by_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('province_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.province')),
            ],
            options={
                'db_table': 'rf_ville',
            },
        ),
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.AddField(
            model_name='address',
            name='commune_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.commune'),
        ),
        migrations.AddField(
            model_name='address',
            name='province_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.province'),
        ),
        migrations.AddField(
            model_name='commune',
            name='ville_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ville'),
        ),
        migrations.AddField(
            model_name='address',
            name='ville_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ville'),
        ),
    ]