import os
from twilio.rest import Client
from dotenv import load_dotenv
from datetime import datetime
import random
import pandas as pd

load_dotenv()

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")

today = (datetime.now().month, datetime.now().day)

df = pd.read_csv('birthdays.csv', encoding='utf-8')

birthdays_dict = df.set_index(['month', 'day']).to_dict(orient='index')

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path, encoding="utf-8") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])
        contents = contents.replace("[NOTES]", birthday_person['notes'])

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=f'whatsapp:{twilio_phone}',
        body=contents,
        to=f"whatsapp:+972{birthday_person['phone']}"
    )
    print(message.status)
