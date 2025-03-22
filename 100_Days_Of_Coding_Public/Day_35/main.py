import requests
from twilio.rest import Client
import os

# endpoint will not work. Havn't subscribed to the API
OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall?"
#api_key = ""
api_key = os.environ.get("OWM_API_KEY")

account_sid = ''
auth_token = ''

weather_params = {
    "lat": ,
    "lon": ,
    "appid": api_key,
}

# response = requests.get(OWN_Endpoint, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()
#
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = True
# for hour_data in weather_data["list"]:
#      condition_code = hour_data["weather"][0]["id"]
#      if int(condition_code) < 700:
#          will_rain = True
    
if will_rain:
    client = Client(account_sid, auth_token)

    # we tested via Whatsapp message and its working. We didn't use wheater app as we don't have a abo there for the api
    message = client.messages.create(
        from_='',
        body="Hello that is a test for coding purpose.",
        to='',
    )

    print(message.status)