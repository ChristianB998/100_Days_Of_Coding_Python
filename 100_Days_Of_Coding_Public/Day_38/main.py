from pandas import pandas as pd
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

############################### Load .env File ###############################
load_dotenv()  # <--- Füge diese Zeile hinzu, um die .env Datei zu laden.

############################### Tokens #################################
authorization_token = os.getenv("AUTHORIZATION_TOKEN")

############################### User Data #################################
GENDER = "male"
WEIGHT_KG = 71
HEIGHT_CM = 196
AGE = 26

############################### Endpoints #################################
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/ea4b1a80a2818ce53219f5508b88c5dc/sheet1/workouts"

############################### User Input #################################
print("NUTRITION_ID:", os.getenv("NUTRITION_ID"))
print("NUTRITION_TOKEN:", os.getenv("NUTRITION_TOKEN"))
exercise_text = input("Tell me which exercises you did: ")

############################### Request Headers #################################
nutritionix_headers = {
    "x-app-id": os.getenv("NUTRITION_ID"),
    "x-app-key": os.getenv("NUTRITION_TOKEN"),
}

sheety_headers = {
    "Authorization": f"Basic {authorization_token}"
}

############################### Request Body #################################
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

############################### Request to Nutritionix API #################################
response = requests.post(exercise_endpoint, headers=nutritionix_headers, json=parameters)
result = response.json()
print("Nutritionix Response:")
print(response.text)

############################### Prepare Data for Sheety #################################
today_date = datetime.now().strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%X")

if "exercises" in result:
    for exercise in result["exercises"]:
        workout_data = {
            "workout": {
                "date": today_date,
                "time": now_time,
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        # Send data to Sheety API
        sheet_response = requests.post(sheet_endpoint, json=workout_data, headers=sheety_headers)
        print("Sheety Response:")
        print(sheet_response.text)
else:
    print("Fehler: Nutritionix hat keine Übungen zurückgegeben.")
