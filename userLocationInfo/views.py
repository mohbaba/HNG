import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from dotenv import load_dotenv

import os

from rest_framework.decorators import api_view

load_dotenv()


# Create your views here.

@api_view(['GET'])
def get_user_info(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    ipinfo = requests.get('http://ip-api.com/json').json()
    ip_address = ipinfo['query']
    location = ipinfo['city']
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={ipinfo['lat']}&lon={ipinfo['lon']}&units=metric&appid={os.environ.get('API_KEY')}").json()
    message = f"Hello, {visitor_name}! the temperature is {weather_data['main']['temp']} degrees in {location}"
    result = {"client_ip": ip_address, "location": location, "message": message}
    return JsonResponse(result, safe=False)
