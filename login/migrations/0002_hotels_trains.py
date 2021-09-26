# Generated by Django 3.1.7 on 2021-04-03 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField(max_length=10, null=True)),
                ('email', models.CharField(max_length=100)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField(null=True)),
                ('guests', models.IntegerField(null=True)),
                ('room_class', models.CharField(max_length=200, null=True)),
                ('no_of_rooms', models.IntegerField(null=True)),
                ('bedtype', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trains',
            fields=[
                ('id', models.AutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('journey_date', models.DateField()),
                ('return_date', models.DateField(null=True)),
                ('no_of_passengers', models.IntegerField(null=True)),
                ('travel_class', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
