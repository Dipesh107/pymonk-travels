# Generated by Django 3.1.7 on 2021-04-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_hotels_trains'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='phone_no',
            field=models.CharField(max_length=12),
        ),
    ]
