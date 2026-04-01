import datetime as dt
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")

today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays_csv = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_csv.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject: Happy Birthday\n\n{contents}")