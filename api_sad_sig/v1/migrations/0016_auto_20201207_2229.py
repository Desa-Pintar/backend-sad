# Generated by Django 2.2.17 on 2020-12-07 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0015_merge_20201207_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sadkeluarga',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sadpenduduk',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sigdesa',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sigdusun',
            name='id',
        ),
        migrations.AlterField(
            model_name='sadkeluarga',
            name='no_kk',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sadpenduduk',
            name='nik',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sigdesa',
            name='nama_desa',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sigdusun',
            name='nama_dusun',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
    ]
