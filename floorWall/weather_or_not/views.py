from django.shortcuts import render
import requests
from .models import Geo
from .forms import GeoForm

def index(request):
    geo_locations = Geo.objects.all() #return all the cities in the database

    url = 'https://api.weather.com/v1/geocode/33.40/-83.42/forecast/daily/3day.json?units=m&language=en-US&apiKey=9d2908c81003444ea908c81003b44ed4'

    if request.method == 'POST': # only true if form is submitted
        form = GeoForm(request.POST) # add actual request data to form for processing
        form.save() # will validate and save if validate

    form = GeoForm()

    weather_data = []

    for geo in geo_locations:

        geo_weather = requests.get(url.format(geo)).json() #request the API data and convert the JSON to Python data types
        
        weather = {
            'geo' : geo,
            'temperature' : geo_weather['main']['temp'],
            'description' : geo_weather['weather'][0]['description'],
            'icon' : geo_weather['weather'][0]['icon']
        }

        weather_data.append(weather) #add the data for the current geo location into our list
    
    context = {'weather_data' : weather_data, 'form' : form}

    return render(request, 'weather_or_not/index.html', context) #returns the index.html template