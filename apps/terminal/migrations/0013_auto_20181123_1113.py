# Generated by Django 2.1.1 on 2018-11-23 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0012_auto_20180816_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='remote_addr',
            field=models.CharField(blank=True, max_length=128, verbose_name='Remote Address'),
        ),
    ]
