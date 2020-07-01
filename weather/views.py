from django.shortcuts import render
import requests
from .models import City
from .forms import CityForms
# Create your views here.
def home(request):
    url='http://api.weatherstack.com/current?access_key=YOUR_API_KEY&query={}'
    # city='Las Vegas'
    # r=requests.get(url.format(city)).json()

    # city_weather={
    #     'city':city,
    #     'temprature':str(r['current']['temperature']),
    #     'description':r['current']['weather_descriptions'][0],
    #     'icon':r['current']['weather_icons'][0]
    # }
    # print(city_weather)
    # return render(request,'weather/home.html')


    if request.method == 'POST':
            form = CityForms(request.POST)
            form.save()

    form = CityForms()

    cities = City.objects.all()

    weather_data = []

    for city in cities:

        r = requests.get(url.format(city)).json()

        city_weather={
            'city':city,
            'temprature':str(r['current']['temperature']),
            'description':r['current']['weather_descriptions'][0],
            'icon':r['current']['weather_icons'][0]
    }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather/home.html', context)