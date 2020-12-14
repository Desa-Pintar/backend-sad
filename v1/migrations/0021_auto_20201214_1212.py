# Generated by Django 2.2.17 on 2020-12-14 05:12

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import v1.models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0020_auto_20201213_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='sigbidang',
            name='geometry',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sigbidang',
            name='pemilik',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='sigbidang',
            name='penguasa',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sadpenduduk',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=v1.models.file_destination),
        ),
    ]
