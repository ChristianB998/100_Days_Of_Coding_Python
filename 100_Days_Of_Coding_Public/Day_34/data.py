import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

response = requests.get("https://opentdb.com/api.php?amount=10", parameters)

response.raise_for_status()

question_data = response.json()["results"]