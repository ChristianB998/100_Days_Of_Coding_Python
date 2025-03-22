import requests
from datetime import datetime

############################### Read Credentials #################################
def load_credentials(filename="credentials.txt"):
    credentials = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.strip().split("=")
            credentials[key] = value
    return credentials

creds = load_credentials()
TOKEN = creds["TOKEN"]
USERNAME = creds["USERNAME"]
############################### Create User #################################
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)

############################### Create Graph on Pixela #################################

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora",	
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Headers will not be seen in the request -> protection meassure 
# https://pixe.la/v1/users/christian19/graphs/graph1.html

#response = requests.post(url=graph_endpoint, json=graph_config, headers = headers)
#print(response.text)


############################### Post Value to the Graph #################################

today = datetime.now()
pixel_quantity = "3"

pixel_endpoint = f"{graph_endpoint}/{graph_config['id']}"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": pixel_quantity,
}

# response = requests.post(url = pixel_endpoint, json = pixel_params, headers= headers)
# print(response.text)

############################### Change existing Value in Graph #################################

change_endpoint = f"{pixel_endpoint}/{today.strftime("%Y%m%d")}"

change_params = {
    "quantity": "5",
}

# response = requests.put(url = change_endpoint, json = change_params, headers= headers)
# print(response.text)

############################### Delete existing Value in Graph #################################

delete_endpoint = f"{pixel_endpoint}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url = delete_endpoint, headers= headers)
# print(response.text)