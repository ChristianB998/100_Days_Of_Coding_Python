import requests

# response:
# 1xx = wait moment dude
# 2xx = Here you go ...
# 3xx = wrong way to go...
# 4xx = You / Me screwed up
# 5xx = they screwed up

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# if response.status_code == 404:
#     raise Exception("That resource does not exists.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")

# short and nice in next line
response.raise_for_status()

longitude = response.json()["iss_position"]["longitude"]
latitude = response.json()["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
