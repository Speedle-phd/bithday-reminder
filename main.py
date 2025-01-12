from email.message import EmailMessage
import os
import smtplib
from datetime import datetime as dt
from dotenv import load_dotenv
import re
from data.data import BIRTHDAY_LIST
from data.greetings import choose_message
#docker run -d -v /docker/birthday-reminder/log:/log -v /docker/birthday-reminder/data:/data birthday-reminder
load_dotenv()

EMAIL : str = os.getenv("EMAIL")
PW : str = os.getenv("EMAIL_PW")

def send_email(message: str, name: str):
    # try:
        print(EMAIL, PW)
        with smtplib.SMTP("smtp.ionos.de", 587, None, 30) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PW)
            em = EmailMessage()
            em.set_content(message)
            em["To"] = "shanks-@gmx.de"
            em["From"] = EMAIL
            em["Subject"] = f"Birthday Reminder for {name}"
            connection.send_message(em)
    # except Exception as e:
    #     with open("log/logger.txt", "a") as file:
    #         file.write(f'{dt.now()}: {e}\n')


def check_birthday():
    for person in BIRTHDAY_LIST:
        if not re.match(r"\d{4}-\d{2}-\d{2}", person["birthday"]):
            print(f"Invalid date format for {person['fname']} {person['lname']}")
            continue
        if person["birthday"].split("-")[1] == dt.now().strftime("%m") and person["birthday"].split("-")[2] == dt.now().strftime("%d"):
            message = choose_message(person)
            name : str = person["fname"] + " " + person["lname"]
            send_email(message, name)   

if __name__ == "__main__":
    check_birthday()
