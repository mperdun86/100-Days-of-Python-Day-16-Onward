import smtplib
import datetime as dt
import random

# Replace these to use
EMAIL = 'EXAMPLE@EMAIL.COM'
RECEIVER = 'ANOTHER@EMAIL.COM'
PASSWORD = 'PASSWORD123'

now = dt.datetime.now()
weekday = now.weekday()

with open('quotes.txt', 'r') as file:
    lines = file.read().splitlines()
# Currently set for google, for other email providers, look up their smtp information
    if weekday == 0:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
            from_addr=EMAIL,
            to_addrs=RECEIVER,
            msg=f'Subject:TEST MESSAGE\n\n{random.choice(lines)}'
            )