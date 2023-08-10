import requests
import json
import socket

from django.http import HttpResponse

from .settings import CONF


def ping(request):
    return HttpResponse("pong")


def get_weather(request):
    weather_data = get_weather_data()

    response_data = {
        'hostname': socket.gethostname(),
        'temperature': weather_data['current']['temperature'],
        'weather_descriptions': weather_data['current']['weather_descriptions'],
        'wind_speed': weather_data['current']['wind_speed'],
        'humidity': weather_data['current']['humidity'],
        'feelslike': weather_data['current']['feelslike']
    }
    return HttpResponse(json.dumps(response_data), status=200)


def get_weather_data():
    url = CONF['weather-url']
    print(url)
    response = requests.get(url)
    return response.json()
