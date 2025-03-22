import requests
from datetime import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
LOOP = True

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def iss_overhead():
    if MY_LAT -5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= + 5:
        return True

def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
def load_credentials(filename="credentials.txt"):
    credentials = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.strip().split("=")
            credentials[key] = value
    return credentials

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while LOOP:
    time.sleep(60)
    if is_dark() and iss_overhead():
        creds = load_credentials()
        my_email = creds["my_email"]
        password = creds["password"]
        target_mail = creds["target_mail"]

        msg = MIMEMultipart()
        msg["From"] = my_email
        msg["To"] = target_mail
        msg["Subject"] = "Look up!!! ISS in view"

        body = f"Look up!!! ISS in view"
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.web.de", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=target_mail, msg=msg.as_string())




