# Generated by Django 2.2.17 on 2021-04-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0010_saddesa_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pegawai',
            name='jabatan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
