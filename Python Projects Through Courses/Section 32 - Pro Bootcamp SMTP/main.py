from datetime import datetime
import random
import pandas as pd
import smtplib

MY_EMAIL = "dimaspektor1224@outlook.com"
MY_PASSWORD = "sefgpoqvuuqtxsfa"

today = (datetime.now().month, datetime.now().day)

df = pd.read_csv('birthdays.csv')
birthdays_dict = df.set_index(['month', 'day']).to_dict(orient='index')
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")

# Mails: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



