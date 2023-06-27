import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")
my_phone = os.getenv("MY_PHONE")

# "lat": -36.848461,
# "lon": 174.763336,

parameters = {
    "lat": 32.011261,
    "lon": 34.774811,
    "appid": os.getenv("APP_ID_API_WEATHER"),
    "exclude": "current, minutely, daily"
}

response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=f'whatsapp:{twilio_phone}',
        body="הולך לרדת גשם. לא לשכוח להביא מטריה ☂️",
        to=f'whatsapp:{my_phone}'
    )
