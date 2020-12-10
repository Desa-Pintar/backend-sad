# Generated by Django 2.2.17 on 2020-12-10 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v1', '0018_auto_20201209_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='SadDusun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('nama', models.CharField(blank=True, max_length=70, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_saddusuns', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='deleted_saddusuns', to=settings.AUTH_USER_MODEL)),
                ('desa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadDesa')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_saddusuns', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'sad_dusun',
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='sadrw',
            name='desa_id',
        ),
        migrations.RemoveField(
            model_name='sadrw',
            name='dusun_dukuh',
        ),
        migrations.AddField(
            model_name='artikel',
            name='tgl',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sadpenduduk',
            name='alamat',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='SadDusunDukuh',
        ),
        migrations.AddField(
            model_name='sadrw',
            name='dusun',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadDusun'),
        ),
    ]
