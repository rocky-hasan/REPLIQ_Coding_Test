# Generated by Django 5.0.1 on 2024-01-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('condition', models.CharField(max_length=100)),
            ],
        ),
    ]
