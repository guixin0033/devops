# Generated by Django 2.2.5 on 2020-10-15 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='datatime',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='test',
            name='local',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='obs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='test',
            name='sfs',
            field=models.IntegerField(),
        ),
    ]
