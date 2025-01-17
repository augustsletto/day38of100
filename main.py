
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

APPLICATION_ID = os.getenv("APPLICATION_ID")
NUTRITIONIX_API = os.getenv("NUTRITIONIX_API")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
SHEETY_API = os.getenv("SHEETY_API")

host_domain = "https://trackapi.nutritionix.com"
endpoint = "/v2/natural/exercise"
sheety_domain = f"https://api.sheety.co/{SHEETY_API}/myWorkouts/workouts"


headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": NUTRITIONIX_API,
}

nutritionix_endpoint = f"{host_domain}/{endpoint}"

nutritionx_config = {
    "query": input("Tell me about your exercise: "),
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 185,
    "age": 27,
}

response = requests.post(url=nutritionix_endpoint, json=nutritionx_config, headers=headers)
# print(response.text)

result = response.json()
print(result)
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    sheet_response = requests.post(sheety_domain, json=sheet_inputs)
    
    print(sheet_response.text)


# sheety_config = {
    
# }

# requests.post()