import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
PASSWORD = os.getenv("PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# connection = smtplib.SMTP("outlook.office365.com")
# connection.starttls()
# connection.login(user=SENDER_EMAIL, password=PASSWORD)
# connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg="Subject: Test Mail\n\nHello")
# connection.close()

with smtplib.SMTP("outlook.office365.com") as connection:
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=SENDER_EMAIL,
        to_addrs=RECEIVER_EMAIL,
        msg="Subject: Test Mail\n\nHello"
    )