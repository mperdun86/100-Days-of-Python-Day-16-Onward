import pandas
import datetime as dt
import random
import smtplib

SENDER = 'SENDERS NAME HERE'
EMAIL = 'SENDING EMAIL HERE'
PASSWORD = 'PASSWORD'

df = pandas.read_csv('birthdays.csv')
birthday_list = df.to_dict(orient="records")

current_time = dt.datetime.now()
today = (current_time.month, current_time.day)

def random_letter(name):
    templates = [
        'letter_templates/letter_1.txt',
        'letter_templates/letter_2.txt',
        'letter_templates/letter_3.txt'
    ]
    file_path = random.choice(templates)
    with open(file_path, 'r') as file:
        return file.read().replace('[NAME]', name).replace('[SENDER]', SENDER)


for person in birthday_list:
    if (person["month"], person["day"]) == today:
        letter = random_letter(person['name'])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(
            from_addr=EMAIL,
            to_addrs=person['email'],
            msg=f'Subject:Happy Birthday!\n\n{letter}'
            )




