# Generated by Django 3.0.5 on 2020-07-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsed_data', '0009_playerdata_party'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
