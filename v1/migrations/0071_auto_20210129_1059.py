# Generated by Django 2.2.17 on 2021-01-29 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v1', '0070_belanja'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegawai',
            name='chip_ektp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sadpenduduk',
            name='alamat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sadpenduduk',
            name='kewarganegaraan',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sadpenduduk',
            name='pekerjaan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sadpenduduk',
            name='pendidikan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Absensi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('jam_masuk', models.DateTimeField(auto_now_add=True, null=True)),
                ('jam_keluar', models.DateTimeField(auto_now=True, null=True)),
                ('alasan_izin', models.CharField(blank=True, max_length=100, null=True)),
                ('jumlah', models.IntegerField(blank=True, max_length=10, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_absensis', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='deleted_absensis', to=settings.AUTH_USER_MODEL)),
                ('pegawai', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.Pegawai')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_absensis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
