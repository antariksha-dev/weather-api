from fastapi import APIRouter, Depends
from app.feature.weather.service import WeatherService 
from app.feature.weather.dependency import get_weather_service

router = APIRouter()

@router.get("/weathers/{city_name}")
def get_weather_by_city(city_name: str, weather_service: WeatherService = Depends(get_weather_service)):
    return weather_service.get_by_city(city_name)
    