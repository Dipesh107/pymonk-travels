from django.db import models

# Create your models here.


class createdFlights(models.Model):
    city_from = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    company_name = models.CharField(max_length=100, null=False)
    no_of_seats = models.IntegerField(null=True)
    pricing = models.CharField(max_length=100, null=False)


class createdTrains(models.Model):
    city_from = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    train_name = models.CharField(max_length=100, null=False)
    no_of_seats = models.IntegerField(null=True)
    pricing = models.IntegerField(null=True)


class myCreatedFlights(models.Model):
    city_from = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    company_name = models.CharField(max_length=100, null=False)
    no_of_seats = models.IntegerField(null=True)
    pricing = models.CharField(max_length=100, null=False)


class myCreatedHotels(models.Model):
    hotel_name = models.CharField(max_length=300, null=False)
    location = models.CharField(max_length=200, null=False)
    avg_prices = models.CharField(max_length=100, null=False)
    facilities = models.CharField(max_length=300, null=False)


class myCreatedTrains(models.Model):
    city_from = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    trains_type = models.CharField(max_length=100, null=False)
    number_of_seats = models.IntegerField(null=True)
    pricing = models.CharField(max_length=100, null=False)


class recordedFlights(models.Model):
    city_from = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    company_name = models.CharField(max_length=100, null=False)
    no_of_seats = models.IntegerField(null=True)
    pricing = models.CharField(max_length=100, null=False)


class bookedFlights(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    mobile = models.CharField(max_length=100, null=False)


class bookedTrains(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    mobile = models.CharField(max_length=100, null=False)


class bookedHotels(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    mobile = models.CharField(max_length=100, null=False)


class MyBookedFlights(models.Model):
    city_from = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)


class holidays(models.Model):
    country = models.CharField(max_length=1000, null=False)
    location = models.CharField(max_length=1000, null=False)
    description = models.CharField(max_length=100000, null=False)
    pricing = models.CharField(max_length=10000, null=False)
    stay = models.CharField(max_length=1000, null=False)
