# Generated by Django 2.2.17 on 2021-01-28 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layananperistiwa', '0004_auto_20210127_0707'),
    ]

    operations = [
        migrations.AddField(
            model_name='sadlahirmati',
            name='nama',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
