from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    Cities = City.objects.all()

    url = 'http://api.openweathermap.org/data/2.5/weather?q={},&units=imperial&appid=c3110ab362f1c1074dc54ee14f1f1d87'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()
    
    weather_data = []

    for city in Cities:

        city_weather = requests.get(url.format(city.name)).json()

        weather = {
            'city' : city.name,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon'],
        }

        weather_data.append(weather)
    
    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather/index.html', context)