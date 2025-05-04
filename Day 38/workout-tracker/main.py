import requests
import json
import datetime as dt
from dotenv import load_dotenv
import os

load_dotenv()
#--------ENVIROMENTAL VARIABLES--------#
SHEETY_URL = os.getenv("SHEETY_URL")
NUTRITIONIX_URL = os.getenv("NUTRITIONIX_URL")
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEETY_TOKEN = os.getenv("SHEETY_TOKEN")
WEIGHT = float(os.getenv("WEIGHT"))
HEIGHT = float(os.getenv("HEIGHT"))
AGE = int(os.getenv("AGE"))
GENDER = os.getenv("GENDER")

#--------USER INPUT--------#
query = input("How did you exercise, and for how long?: ")

parameters = {
    "query": query,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(NUTRITIONIX_URL, headers=headers, json=parameters)
exercise_info = response.json()

now = dt.datetime.now()

new_entry = {
    "workout": {
        "date": now.strftime("%Y-%m-%d"),
        "time": now.strftime("%H:%M:%S"),
        "duration": exercise_info["exercises"][0]["duration_min"],
        "exercise": exercise_info["exercises"][0]["name"].title(),
        "calories": exercise_info["exercises"][0]["nf_calories"]
    }
}

sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

s_response = requests.post(SHEETY_URL, headers=sheety_headers, data=json.dumps(new_entry))

#--------RESPONSE HANDLING--------#
if s_response.status_code in [200, 201]:
    workout_data = s_response.json()
    print("Workout logged:")
    print(workout_data["workout"])
else:
    print("Error:", s_response.status_code, s_response.text)
