# Generated by Django 2.1.7 on 2020-11-24 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=20)),
                ('path', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
            ],
        ),
    ]