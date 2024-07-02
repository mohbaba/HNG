import requests
from django.http import JsonResponse, HttpRequest
from dotenv import load_dotenv
import os
from rest_framework.decorators import api_view

load_dotenv()


# Create your views here.

@api_view(['GET'])
def get_user_info(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    visitor_ip_address = get_visitor_ip_address(request, request.META.get('HTTP_X_FORWARDED_FOR'))
    ipinfo = requests.get(f'http://ip-api.com/json/{visitor_ip_address}').json()
    ip_address = ipinfo['query']
    location = ipinfo['city']
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={ipinfo['lat']}&lon={ipinfo['lon']}&units=metric&appid={os.environ.get('API_KEY')}").json()
    message = f"Hello, {visitor_name}! the temperature is {weather_data['main']['temp']} degrees in {location}"
    result = {"client_ip": ip_address, "location": location, "message": message}
    return JsonResponse(result, safe=False)


def get_visitor_ip_address(request, visitor_ip_address):
    if visitor_ip_address:
        visitor_ip = visitor_ip_address.split(',')[0]
        return visitor_ip
    return request.META.get('REMOTE_ADDR')
