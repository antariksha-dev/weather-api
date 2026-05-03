import httpx
from app.feature.weather.models import WeatherResponse
import os

base_url='https://api.openweathermap.org/data/2.5'

class WeatherService:
    def get_by_city(self, city_name: str):
        api_token = os.getenv("API_TOKEN")  
        with httpx.Client() as client:
            http = client.get(f'{base_url}/weather?q={city_name}&appid={api_token}')
            data = http.json()
            temp = round(data.get("main").get("temp") - 273.15, 2)
            return WeatherResponse(city=city_name, temperature=temp)