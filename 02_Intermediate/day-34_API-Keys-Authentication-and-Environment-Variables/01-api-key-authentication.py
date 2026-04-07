import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
LAT = float(os.getenv("LATITUDE"))
LONG = float(os.getenv("LONGITUDE"))

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY
}

#response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LONG}&appid={API_KEY}")
print(response.status_code)