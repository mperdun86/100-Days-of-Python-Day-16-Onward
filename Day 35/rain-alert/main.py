import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = 'key here'
LATITUDE = 0.00000000
LONGITUDE = 0.0000000
PARAMETERS = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid":OWM_API_KEY,
    "cnt": 4,
}
TWILIO_ACCOUNT_SID = 'ssid here'
TWILIO_AUTH_TOKEN = 'auth token here'

response = requests.get(OWM_ENDPOINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()


bring_umbrella = False

for item in weather_data["list"]:
    code = item["weather"][0]["id"]
    if code < 700:
        bring_umbrella = True
        break

if bring_umbrella:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        from_='+15551234444',
        body='Grab an Umbrella!',
        to='+15551234444'
    )

