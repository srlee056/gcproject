# Generated by Django 3.0.5 on 2020-07-28 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0004_auto_20200727_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerdata',
            name='mrFloor',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
