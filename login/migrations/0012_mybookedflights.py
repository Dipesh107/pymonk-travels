# Generated by Django 3.1.7 on 2021-04-12 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_bookedhotels_bookedtrains'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyBookedFlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]