# Generated by Django 2.1.7 on 2021-01-04 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0014_auto_20210104_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project1',
            name='project',
            field=models.CharField(max_length=100),
        ),
    ]