# Generated by Django 2.2.17 on 2020-12-17 03:49

from django.db import migrations, models
import v1.models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0030_auto_20201217_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegawai',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to=v1.models.file_destination),
        ),
    ]
