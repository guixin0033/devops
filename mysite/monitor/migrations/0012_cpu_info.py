# Generated by Django 2.1.7 on 2020-12-31 01:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_memory_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='cpu_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=20)),
                ('cpu_percent', models.FloatField(default=0)),
                ('cpu_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]