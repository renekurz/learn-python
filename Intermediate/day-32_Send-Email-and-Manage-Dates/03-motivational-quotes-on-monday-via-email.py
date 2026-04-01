import smtplib
import os
from dotenv import load_dotenv
import datetime as dt
import random

if dt.datetime.now().weekday() == 0:
    load_dotenv()

    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()
        text_to_send = random.choice(quotes)

        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject: Have a nice Monday\n\n{text_to_send}"
            )