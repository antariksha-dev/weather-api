from fastapi import FastAPI
from app.feature.weather.router import router as weather_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(weather_router)