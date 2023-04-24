#Monday Motivation Project
import smtplib
import datetime as dt
import random

MY_EMAIL = "dimaspektor1224@outlook.com"
MY_PASSWORD = "sefgpoqvuuqtxsfa"

now = dt.datetime.now()

weekday = now.weekday()
if weekday == 5:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# # Sending Email with Python
# with smtplib.SMTP("smtp.office365.com") as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="dimaspektor1224@outlook.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
























## Working with date and time in Python
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)