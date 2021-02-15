# Generated by Django 2.2.17 on 2021-02-15 03:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0085_cctv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sigrt2',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='sigrt2',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='sigrt2',
            name='sig_rw2',
        ),
        migrations.RemoveField(
            model_name='sigrt2',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='sigrw2',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='sigrw2',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='sigrw2',
            name='sig_dukuh2',
        ),
        migrations.RemoveField(
            model_name='sigrw2',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='sigsadbidang2',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='sigsadbidang2',
            name='deleted_by',
        ),
        migrations.RemoveField(
            model_name='sigsadbidang2',
            name='sad_penduduk',
        ),
        migrations.RemoveField(
            model_name='sigsadbidang2',
            name='sig_bidang2',
        ),
        migrations.RemoveField(
            model_name='sigsadbidang2',
            name='updated_by',
        ),
        migrations.RenameField(
            model_name='potensi',
            old_name='alamat',
            new_name='no_telp',
        ),
        migrations.AddField(
            model_name='sigbidang',
            name='latitude',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sigbidang',
            name='longitude',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='SigBidang2',
        ),
        migrations.DeleteModel(
            name='SigRt2',
        ),
        migrations.DeleteModel(
            name='SigRw2',
        ),
        migrations.DeleteModel(
            name='SigSadBidang2',
        ),
    ]
