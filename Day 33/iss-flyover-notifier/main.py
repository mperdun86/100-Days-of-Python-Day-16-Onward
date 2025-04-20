import requests
from datetime import datetime
import time
import smtplib

# --------CONSTANTS--------#
EMAIL = 'example@email.com'
RECEIVER = 'example@email.com'
PASSWORD = 'password123'
TIME_ZONE = 'timezone'
MY_LAT = 0.000000
MY_LONG = 0.000000
PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": TIME_ZONE,
}

# --------FUNCTIONS--------#
def distance_detector(my_lat, my_long):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if abs(iss_lat - my_lat) <= 5 and abs(iss_long - my_long) <= 5:
        return True
    else:
        return False


def darkness_detector():
    response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour >= sunset or time_now.hour < sunrise:
        return True
    else:
        return False

# --------MAIN LOOP--------#
while True:
    try:
        if distance_detector(MY_LAT, MY_LONG) and darkness_detector():
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=RECEIVER,
                    msg=f'Subject:Go outside!\n\nThe ISS is going to be flying over soon!'
                )
        else:
            print("ISS not in range")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

    time.sleep(60)
