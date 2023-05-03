import requests
from twilio.rest import Client

account_sid = "AC237bc0db2e93f30459b8939b5d955d3a"
auth_token = "b612ac166e3987862d7e6df9e84513b2"


parameters = {
    "lat": -36.848461,
    "lon": 174.763336,
    "appid": "262ca3e8ba5bf146949d1a9f2e8b6d1b",
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
        from_='whatsapp:+14155238886',
        body="הולך לרדת גשם. לא לשכוח להביא מטריה ☂️",
        to='whatsapp:+972507999325'
    )
    print(message.status)
