import smtplib
import datetime as dt
import random

MY_EMAIL = "aryan07chaudhari@gmail.com"
PASSWORD = "dvfx hoeg bwvx obpd"


# TO GET WEEK DAY
now = dt.datetime.now()
day_of_week = now.weekday()


# SENDING MAIL IF DAY OF WEEK IS MONDAY
if day_of_week == 0:
    # TO GET RANDOM QUOTES
    with open("quotes.txt") as file:
        for text in file:
            quotes_list = file.readlines()
            random_quote = random.choice(quotes_list)

    # FOR SEND MAIL
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # starttls make our connection secure
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="bunnys.laptop.00@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{random_quote}"
        )

