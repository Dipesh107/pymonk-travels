# Generated by Django 3.1.7 on 2021-04-05 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20210403_1834'),
    ]

    operations = [
        migrations.CreateModel(
            name='createdFlights',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('no_of_seats', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='createdTrains',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('train_name', models.CharField(max_length=100)),
                ('no_of_seats', models.IntegerField(null=True)),
            ],
        ),
    ]
