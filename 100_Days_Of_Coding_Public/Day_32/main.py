import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def load_credentials(filename="credentials.txt"):
    credentials = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            key, value = line.strip().split("=")
            credentials[key] = value
    return credentials
# there is always a simpler way, if you want to make it harder, then just do it like me...
def load_quotas(filename="quotes.txt"):
    #quotes = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            all_quotes = file.readlines()
            quotes = random.choice(all_quotes)
            #if " - " in line:
                #quote, author = line.rsplit(" - ", 1)
                #quotes.append((quote.strip(), author.strip()))
    #return random.choice(quotes)
    return quotes

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    load_quotas()

creds = load_credentials()
my_email = creds["my_email"]
password = creds["password"]
target_mail = creds["target_mail"]

msg = MIMEMultipart()
msg["From"] = my_email
msg["To"] = target_mail
msg["Subject"] = "Monday Motivation"
#msg["Date"] = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S +0000')  # UTC-Zeit

body = f"{load_quotas()}"
msg.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.web.de", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=target_mail, msg=msg.as_string())
    #connection.sendmail(from_addr=my_email,
    #                    to_addrs=target_mail,
    #                    msg="Subject:Hello\n\nThis is not a spam")