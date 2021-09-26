# Generated by Django 3.1.7 on 2021-04-07 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20210407_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='myCreatedFlights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_from', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('no_of_seats', models.IntegerField(null=True)),
                ('pricing', models.CharField(max_length=100)),
            ],
        ),
    ]