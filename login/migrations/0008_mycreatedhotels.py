# Generated by Django 3.1.7 on 2021-04-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_mycreatedflights'),
    ]

    operations = [
        migrations.CreateModel(
            name='myCreatedHotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=200)),
                ('avg_prices', models.CharField(max_length=100)),
                ('facilities', models.CharField(max_length=300)),
            ],
        ),
    ]
