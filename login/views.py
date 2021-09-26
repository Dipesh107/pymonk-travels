from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from login.models import myCreatedFlights
from login.models import myCreatedTrains
from login.models import myCreatedHotels
from django.db.models import Q
from .forms import afterbookForm
from .forms import afterbookFormTrains
from .forms import afterbookFormHotels
from .forms import myBookedFlights
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

# Create your views here.
from .forms import CreateUserForm


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password not found')
            return redirect('login')

    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('home')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')
            messages.success(request, "Account has been created for " + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def home(request):
    return render(request, 'home.html')


flightcity = ""
flightdest = ""
flightdate = ""
traincity = ""
traindest = ""
traindate = ""
hotellocation = ""
hoteldate = ""


def flights(request):
    if 'city_from' in request.GET:
        global flightcity
        city_from = request.GET['city_from']
        flightcity = city_from
        global flightdest
        destination = request.GET['destination']
        flightdest = destination
        global flightdate
        date = request.GET['jdate']
        flightdate = date
        results = myCreatedFlights.objects.filter(
            Q(city_from__icontains=city_from), Q(destination__icontains=destination))

        return render(request, 'bookFlight.html', {'data': results})
    else:
        return render(request, 'flights.html')


def account(request):
    context = {'city': flightcity, 'dest': flightdest, 'date': flightdate, 'traincity': traincity,
               'traindest': traindest, 'traindate': traindate, 'hotellocation': hotellocation, 'hoteldate': hoteldate}
    return render(request, 'account.html', context)


def hotels(request):
    if 'location' in request.GET:
        global hotellocation
        location = request.GET['location']
        hotellocation = location
        global hoteldate
        date = request.GET['bookdate']
        hoteldate = date
        results = myCreatedHotels.objects.filter(
            Q(location__icontains=location))
        return render(request, 'bookHotel.html', {'data': results})
    else:
        return render(request, 'hotels.html')


def trains(request):
    if 'city_from' in request.GET:
        global traincity
        city_from = request.GET['city_from']
        traincity = city_from
        global traindest
        destination = request.GET['destination']
        traindest = destination
        global traindate
        date = request.GET['journeyDate']
        traindate = date
        results = myCreatedTrains.objects.filter(
            Q(city_from__icontains=city_from), Q(destination__icontains=destination))
        return render(request, 'bookTrain.html', {'data': results})
    else:
        return render(request, 'trains.html')


def review(request):

    if request.method == 'POST':
        name = request.POST['sender_name']
        number = request.POST['sender_number']
        email = request.POST['sender_email']
        message = request.POST['message']
        result = "Hello " + name + ",Thank You For reviewing us... "
        context = {'name': name, 'number': number,
                   'message': message, 'result': result, 'email': email}

        html_content = render_to_string('email_template.html', context)
        text_content = strip_tags(html_content)

        email = EmailMultiAlternatives(
            "Thank You For reviewing us...",
            text_content,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send()
        return redirect('/reviewthank')

    return render(request, 'review.html')


def payment(request):
    return render(request, 'payment.html')


def showFlights(request):
    # if request.method == 'POST':
    # search_item = request.GET['search']
    # result = myCreatedFlights.objects.filter(
    # Q(city_from__icontains=search_item))

    results = myCreatedFlights.objects.all()
    return render(request, 'bookFlight.html', {'data': results})


def showTrains(request):
    results = myCreatedTrains.objects.all()
    return render(request, 'bookTrain.html', {'data': results})


def showHotels(request):
    results = myCreatedHotels.objects.all()
    return render(request, 'bookHotel.html', {'data': results})


def afterbook(request):
    form = afterbookForm()

    if request.method == 'POST':
        form = afterbookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'afterbook.html', context)


def afterbookTrains(request):
    form = afterbookFormTrains()

    if request.method == 'POST':
        form = afterbookFormTrains(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'afterbook.html', context)


def afterbookHotels(request):
    form = afterbookFormHotels()

    if request.method == 'POST':
        form = afterbookFormHotels(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')

    context = {'form': form}
    return render(request, 'afterbook.html', context)


def thank(request):
    return render(request, 'thank.html')


def reviewthank(request):
    return render(request, 'reviewthank.html')
