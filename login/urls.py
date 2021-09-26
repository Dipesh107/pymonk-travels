from django.contrib import admin
from django.urls import path
from login import views

admin.site.site_header = "PyMonk Travel Admin"
admin.site.site_title = "PyMonk Travel Admin Portal"
admin.site.index_title = "Welcome to PyMonk Travel"

urlpatterns = [
    path("", views.home, name='home'),
    path("flights", views.flights, name='flights'),
    path("hotels", views.hotels, name='hotels'),
    path("trains", views.trains, name='trains'),
    path("review", views.review, name='review'),
    path("account", views.account, name='account'),
    path("login", views.loginPage, name='login'),
    path("logout", views.logoutPage, name='logout'),
    path("register", views.register, name='register'),
    path("payment", views.payment, name='payment'),
    path("bookflight", views.showFlights, name='bookflight'),
    path("booktrain", views.showTrains, name='booktrain'),
    path("bookhotel", views.showHotels, name='bookhotel'),
    path("afterbook", views.afterbook, name='afterbook'),
    path("thank", views.thank, name='thank'),
    path("reviewthank", views.reviewthank, name='reviewthank'),
]
