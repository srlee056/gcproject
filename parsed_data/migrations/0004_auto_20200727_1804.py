# Generated by Django 3.0.5 on 2020-07-27 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0003_auto_20200727_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerdata',
            name='imgSrc',
            field=models.CharField(max_length=400),
        ),
    ]