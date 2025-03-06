import datetime as dt
import pandas as pd
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

now = dt.datetime.now()
day = now.day
month = now.month

def load_credentials(filename="credentials.txt"):
    credentials = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.strip().split("=")
            credentials[key] = value
    return credentials

df = pd.read_csv("birthdays.csv")

birthday_today = df[(df["day"] == day) & (df["month"] == month)]

if not birthday_today.empty:
    creds = load_credentials()
    my_email = creds["my_email"]
    password = creds["password"]


    with smtplib.SMTP("smtp.web.de", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        for _, row in birthday_today.iterrows():
            name = row["name"]
            target_mail = row["email"]

            letter_number = random.randint(1, 3)
            input_path = f"letter_templates/letter_{letter_number}.txt"

            with open(input_path, "r", encoding="utf-8") as file:
                content = file.read()

            updated_content = content.replace("[NAME]", name)

            msg = MIMEMultipart()
            msg["From"] = my_email
            msg["To"] = target_mail
            msg["Subject"] = f"Happy Birthday, {name}! 🎉"

            msg.attach(MIMEText(updated_content, "plain"))

            connection.sendmail(
                from_addr=my_email,
                to_addrs=target_mail,
                msg=msg.as_string()
            )

            print(f"🎉 Birthday mail {name} ({target_mail}) was send!")

else:
    print("Nobodys birthday today.")
