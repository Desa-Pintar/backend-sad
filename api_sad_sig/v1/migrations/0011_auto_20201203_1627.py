# Generated by Django 2.2.17 on 2020-12-03 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0010_sigsadbidang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sigbidang',
            name='sig_dukuh2',
        ),
        migrations.RemoveField(
            model_name='sigbidang2',
            name='sig_dukuh2',
        ),
        migrations.AddField(
            model_name='sigbidang',
            name='sig_rt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigRt'),
        ),
        migrations.AddField(
            model_name='sigbidang2',
            name='sig_rt2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigRt2'),
        ),
        migrations.CreateModel(
            name='SigSadBidang2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pemilik', models.CharField(blank=True, max_length=100, null=True)),
                ('penguasa', models.CharField(blank=True, max_length=100, null=True)),
                ('sad_penduduk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SadPenduduk')),
                ('sig_bidang2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='v1.SigBidang2')),
            ],
            options={
                'db_table': 'sig_sad_bidang2',
            },
        ),
    ]
