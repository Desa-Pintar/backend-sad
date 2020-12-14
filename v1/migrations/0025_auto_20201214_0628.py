# Generated by Django 2.2.17 on 2020-12-14 06:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('v1', '0024_auto_20201214_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='suratdomisili',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='suratdomisili',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_suratdomisilis', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='suratdomisili',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='suratdomisili',
            name='deleted_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='deleted_suratdomisilis', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='suratdomisili',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='suratdomisili',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_suratdomisilis', to=settings.AUTH_USER_MODEL),
        ),
    ]
