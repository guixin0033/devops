# Generated by Django 2.1.7 on 2021-01-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0026_get_obs_dir_obs_dir_spending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='get_obs_dir',
            name='obs_dir_path',
            field=models.CharField(max_length=100),
        ),
    ]
