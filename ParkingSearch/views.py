from django.shortcuts import render
from django.http import *
# Create your views here.
from .models import Parking


def main(request):
    return HttpResponse('Main page')


def detail(request):
    data = Parking.objects.all()

    return render(request, 'main.html', {'data': data})


def db(request):
    data = Parking.objects.all()
    lon = Parking.objects.values('longitude')
    lat = Parking.objects.values('latitude')
    return render(request, 'db.html', {'data': data, 'lon': lon, 'lat': lat})
